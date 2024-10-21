const express = require("express");
const cors = require("cors");
const { exec } = require("child_process");
const app = express();

app.use(cors());
app.use(express.json());

// POST route for receiving questions & sending responses
app.post("/api/chat", (req, res) => {
  const userQuestion = req.body.question;

  // executing ai_assistant.py to handle LangChain and AI model
  exec(
    `python3 ai_assistant.py "${userQuestion}"`,
    (error, stdout, stderr) => {
      if (error) {
        console.error(`Error executing Python: ${error.message}`);
        return res.status(500).send("Server error");
      }
      if (stderr) {
        console.error(`Python error: ${stderr}`);
        return res.status(500).send("Model error");
      }
      res.json({ response: stdout.trim() });
    }
  );
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
