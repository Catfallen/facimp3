import { useState } from "react";

import { Text, View, Button } from "react-native";



export default function Index() {
  const dices = ["⚀","⚁","⚂","⚃","⚄","⚅"]
  const [texto,setTexto] = useState(dices[1])

  return (
    <View
      style={{
        flex: 1,
        alignItems: "center",
        flexDirection: "column"
      }}
    >
      <Text style={{ fontSize: 48, color: "black", fontWeight: "bold", marginBottom: 40 }}>
        Lançamento de dados
      </Text>
      <Text style={{ fontSize: 96, color: "black", fontWeight: "bold", marginBottom: 20 }}>{texto}</Text>
      <Button title="Lançar dado" onPress={() => {
        setTexto(dices[2])
      }} />
    </View>
  );
}
