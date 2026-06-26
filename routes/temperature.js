const express = require("express");
const router = express.Router();

router.get("/", (req, res) => {
  res.render("temperature", {
    celsius: null,
    fahrenheit: null,
  });
});

router.post("/", (req, res) => {
  const celsius = Number(req.body.celsius);
  const fahrenheit = (celsius * 9) / 5 + 32;

  res.render("temperature", {
    celsius,
    fahrenheit,
  });
});

module.exports = router;
