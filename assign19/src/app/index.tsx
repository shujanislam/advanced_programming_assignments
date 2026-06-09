import React, { useState } from 'react';
import { StyleSheet, Text, TouchableOpacity, View } from 'react-native';

type AppTheme = 'light' | 'dark';

const App = () => {
  const [count, setCount] = useState(0);
  const [theme, setTheme] = useState<AppTheme>('dark');

  const increment = () => setCount(prevCount => prevCount + 1);

  const decrement = () => {
    if (count <= 1) {
      setCount(0);
    } else {
      setCount(prevCount => prevCount - 1);
    }
  };

  const reset = () => setCount(0);

  const changeTheme = () => {
    if (theme === 'dark') {
      setTheme('light');
    } else {
      setTheme('dark');
    }
  };

  const isDark = theme === 'dark';
  const backgroundColor = isDark ? '#000000' : '#FFFFFF';
  const textColor = isDark ? '#FFFFFF' : '#000000';

  return (
    <View style={[styles.container, { backgroundColor }]}> 
      <View style={[styles.card, { borderColor: textColor }]}> 
        <Text style={[styles.title, { color: textColor }]}>Digital Counter</Text>
        <Text style={[styles.count, { color: textColor }]}>{count}</Text>

        <TouchableOpacity style={[styles.button, { backgroundColor, borderColor: textColor }]} onPress={increment}>
          <Text style={[styles.buttonText, { color: textColor }]}>Increment</Text>
        </TouchableOpacity>

        <TouchableOpacity style={[styles.button, { backgroundColor, borderColor: textColor }]} onPress={decrement}>
          <Text style={[styles.buttonText, { color: textColor }]}>Decrement</Text>
        </TouchableOpacity>

        <TouchableOpacity style={[styles.button, { backgroundColor, borderColor: textColor }]} onPress={reset}>
          <Text style={[styles.buttonText, { color: textColor }]}>Reset</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.button, styles.themeButton, { backgroundColor, borderColor: textColor }]}
          onPress={changeTheme}>
          <Text style={[styles.buttonText, { color: textColor }]}>Theme: {theme}</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 24,
  },
  card: {
    width: '100%',
    maxWidth: 360,
    borderRadius: 18,
    padding: 20,
    borderWidth: 1,
    alignItems: 'center',
    gap: 10,
  },
  title: {
    fontSize: 30,
    fontWeight: '700',
  },
  count: {
    fontSize: 56,
    fontWeight: '800',
    marginBottom: 8,
  },
  button: {
    alignItems: 'center',
    width: '100%',
    paddingVertical: 12,
    borderRadius: 10,
    borderWidth: 1,
  },
  themeButton: {
    marginTop: 8,
  },
  buttonText: {
    fontSize: 16,
    fontWeight: '600',
  },
});

export default App;
