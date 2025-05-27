import React from 'react';
import { StyleSheet, Text, Image } from 'react-native';
import { ThemedView } from '@/components/ThemedView';

export default function MainScreen() {
  return (
    <ThemedView style={styles.container}>
      <Image
        source={{ uri: 'https://picsum.photos/200/300' }} 
        style={styles.image}
        resizeMode="contain"
      />
      <Text style={styles.title}>This is the main single screen</Text>
    </ThemedView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff', // nền trắng
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
  },
  image: {
    width: 150,
    height: 150,
    marginBottom: 20,
  },
  title: {
    fontSize: 20,
  },
});
