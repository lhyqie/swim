(function () {
  var COOKIE_NAME = "swim_favorite_swimmers";
  var COOKIE_EXPIRES = "Fri, 31 Dec 9999 23:59:59 GMT";
  var MAX_FAVORITES = 50;

  function readCookie(name) {
    var prefix = name + "=";
    var parts = document.cookie ? document.cookie.split("; ") : [];
    for (var i = 0; i < parts.length; i++) {
      if (parts[i].indexOf(prefix) == 0) {
        return parts[i].substring(prefix.length);
      }
    }
    return "";
  }

  function normalizeFavorite(favorite) {
    favorite = favorite || {};
    var id = String(favorite.id || favorite.i || "").trim();
    return {
      id: id,
      name: String(favorite.name || favorite.n || id).trim(),
      team: String(favorite.team || favorite.t || "").trim(),
      age: String(favorite.age || favorite.a || "").trim(),
      sex: String(favorite.sex || favorite.s || "").trim()
    };
  }

  function compactFavorite(favorite) {
    return {
      i: favorite.id,
      n: favorite.name,
      t: favorite.team,
      a: favorite.age,
      s: favorite.sex
    };
  }

  function getFavorites() {
    var raw = readCookie(COOKIE_NAME);
    if (!raw) {
      return [];
    }
    try {
      var parsed = JSON.parse(decodeURIComponent(raw));
      if (!Array.isArray(parsed)) {
        return [];
      }
      return parsed.map(normalizeFavorite).filter(function (favorite) {
        return favorite.id.length > 0;
      });
    } catch (error) {
      return [];
    }
  }

  function saveFavorites(favorites) {
    var seen = {};
    var normalized = [];
    favorites.forEach(function (favorite) {
      var next = normalizeFavorite(favorite);
      if (next.id && !seen[next.id]) {
        seen[next.id] = true;
        normalized.push(next);
      }
    });

    var compact = normalized.slice(0, MAX_FAVORITES).map(compactFavorite);
    document.cookie = COOKIE_NAME + "=" + encodeURIComponent(JSON.stringify(compact)) +
      "; expires=" + COOKIE_EXPIRES + "; path=/; SameSite=Lax";
  }

  function hasFavorite(id) {
    id = String(id || "");
    return getFavorites().some(function (favorite) {
      return favorite.id == id;
    });
  }

  function addFavorite(favorite) {
    var next = normalizeFavorite(favorite);
    if (!next.id) {
      return;
    }
    var favorites = getFavorites().filter(function (existing) {
      return existing.id != next.id;
    });
    favorites.unshift(next);
    saveFavorites(favorites);
  }

  function removeFavorite(id) {
    id = String(id || "");
    saveFavorites(getFavorites().filter(function (favorite) {
      return favorite.id != id;
    }));
  }

  function removeFavoriteById(id) {
    id = String(id || "");
    var removed = getFavorites().filter(function (favorite) {
      return favorite.id == id;
    })[0];
    removeFavorite(id);
    refreshFavoriteButtons(document);
    document.dispatchEvent(new CustomEvent("swim:favorites-changed", {
      detail: { favorite: removed || { id: id }, active: false }
    }));
  }

  function toggleFavorite(favorite) {
    var next = normalizeFavorite(favorite);
    if (!next.id) {
      return false;
    }
    if (hasFavorite(next.id)) {
      removeFavorite(next.id);
      return false;
    }
    addFavorite(next);
    return true;
  }

  function favoriteFromButton(button) {
    return normalizeFavorite({
      id: button.dataset.favoriteId,
      name: button.dataset.favoriteName,
      team: button.dataset.favoriteTeam,
      age: button.dataset.favoriteAge,
      sex: button.dataset.favoriteSex
    });
  }

  function favoriteMeta(favorite) {
    var parts = [];
    if (favorite.age || favorite.sex) {
      parts.push([favorite.age, favorite.sex].filter(Boolean).join(" "));
    }
    if (favorite.team) {
      parts.push(favorite.team);
    }
    return parts.join(" - ");
  }

  function favoriteOptionText(favorite) {
    var meta = favoriteMeta(favorite);
    return meta ? favorite.name + " - " + meta : favorite.name;
  }

  function updateFavoriteButton(button) {
    var active = hasFavorite(button.dataset.favoriteId);
    var textMode = button.dataset.favoriteMode == "text";
    button.classList.toggle("is-favorite", active);
    button.setAttribute("aria-pressed", active ? "true" : "false");
    button.textContent = active ? (textMode ? "Favorited" : "Saved") : (textMode ? "Favorite" : "Save");
    button.title = active ? "Remove from favorites" : "Add to favorites";
  }

  function refreshFavoriteButtons(root) {
    root = root || document;
    root.querySelectorAll("[data-favorite-id]").forEach(updateFavoriteButton);
  }

  function toggleFavoriteFromButton(button) {
    var favorite = favoriteFromButton(button);
    var active = toggleFavorite(favorite);
    refreshFavoriteButtons(document);
    document.dispatchEvent(new CustomEvent("swim:favorites-changed", {
      detail: { favorite: favorite, active: active }
    }));
  }

  document.addEventListener("DOMContentLoaded", function () {
    refreshFavoriteButtons(document);
  });

  document.addEventListener("htmx:afterSwap", function (event) {
    refreshFavoriteButtons(event.target || document);
  });

  window.SwimFavorites = {
    getFavorites: getFavorites,
    favoriteMeta: favoriteMeta,
    favoriteOptionText: favoriteOptionText,
    removeFavorite: removeFavoriteById,
    refreshFavoriteButtons: refreshFavoriteButtons
  };
  window.toggleFavoriteFromButton = toggleFavoriteFromButton;
})();
