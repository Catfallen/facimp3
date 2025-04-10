import React, {useState} from "react";
import { Text, View, TextInput, StyleSheet } from "react-native";

export default function Index() {
  const [texto,setTexto] = useState("")
  return (
    <View style = {styles.container}>
      <Text style = {styles.label}></Text>
      <TextInput
        style = {styles.input}//pega os estilos da classe input
        placeholder="Escreva aqui"
        value={texto}
        onChangeText={setTexto}
      >
      </TextInput>
      <Text style = {styles.resultado}>Você digitou: {texto}</Text>
    </View>
  );
  
}

const styles = StyleSheet.create({
  container: {padding:20,marginTop: 50}, //containter
  label: {fontSize:16, marginBottom:5},
  input: {
    borderWidth: 1,
    borderColor:"#ccc", 
    padding: 10, 
    borderRadius: 5, 
    fontSize:16},
  resultado : {
    marginTop: 10,
    fontSize: 16, 
    fontWeight: "bold"
  }
});