setTimeout(function () {
    if (location.protocol !== "https:") {
      location.protocol = "https:";
    } else {
      window.location.replace("/home");
    };
  }, 1000);