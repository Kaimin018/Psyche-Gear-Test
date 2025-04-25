import { useState } from 'react'

const questions = [
  {
    question: '你在攀岩館最常做什麼？',
    options: [
      { text: '幫朋友刷點', result: '刷子' },
      { text: '給大家分享岩點情報', result: '螢光筆' },
      { text: '準備能量棒和水給大家', result: '能量棒' },
      { text: '默默補粉、備繩、收裝備', result: '繩子' },
    ]
  },
  {
    question: '你的攀岩風格？',
    options: [
      { text: '果斷踩點、暴力爆發', result: '岩鞋' },
      { text: '穩穩爬、有風格地完成', result: '吊帶' },
      { text: '總是在最後成功，堅持到底', result: '白貼' },
      { text: '無論幾次都願意再來一次', result: '粉袋' },
    ]
  }
]

const results = {
  '粉袋': '你是氣氛製造者，隨時準備出粉，讓現場熱起來。',
  '岩鞋': '你是衝鋒者，總是第一個挑戰最困難的點。',
  '吊帶': '你是穩定支撐型，夥伴信任的後盾。',
  '白貼': '你是堅持到底的人，傷痛也不放棄夢想。',
  '刷子': '你是完美主義的助攻者，總想讓一切更好爬。',
  '能量棒': '你是臨時補給站，總在大家快撐不住時出現。',
  '繩子': '你是沉默而可靠的連結者，支持整場冒險。',
  '螢光筆': '你總能指出重點，是大家的路線指引者。'
}

export default function ClimbingQuiz() {
  const [current, setCurrent] = useState(0)
  const [answers, setAnswers] = useState([])
  const [showResult, setShowResult] = useState(false)

  const handleAnswer = (result) => {
    const newAnswers = [...answers, result]
    if (current + 1 < questions.length) {
      setAnswers(newAnswers)
      setCurrent(current + 1)
    } else {
      setAnswers(newAnswers)
      setShowResult(true)
    }
  }

  const countResult = () => {
    const count = {}
    answers.forEach(ans => {
      count[ans] = (count[ans] || 0) + 1
    })
    return Object.entries(count).sort((a, b) => b[1] - a[1])[0][0]
  }

  if (showResult) {
    const topResult = countResult()
    return (
      <div className="p-4 text-center">
        <h1 className="text-xl font-bold mb-4">你是：{topResult}</h1>
        <p className="mb-4">{results[topResult]}</p>
        <button className="bg-blue-500 text-white px-4 py-2 rounded" onClick={() => { setCurrent(0); setAnswers([]); setShowResult(false) }}>再測一次</button>
      </div>
    )
  }

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">{questions[current].question}</h1>
      <div className="space-y-2">
        {questions[current].options.map((opt, idx) => (
          <button
            key={idx}
            className="block w-full bg-gray-200 hover:bg-gray-300 px-4 py-2 rounded"
            onClick={() => handleAnswer(opt.result)}>
            {opt.text}
          </button>
        ))}
      </div>
    </div>
  )
}
