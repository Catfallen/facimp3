import { useFonts } from "expo-font";
import React, {useState} from "react";
import { Text, View, TextInput, StyleSheet } from "react-native";

export default function Index() {
    const [isLoadedFonts] = useFonts(
        {
            "GeneralSans-400": require("/")
        }
    )
    return (
    <View>

    </View>
  );
  
}

