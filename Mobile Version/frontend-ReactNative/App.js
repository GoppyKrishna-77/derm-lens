import GetStartedPage from './Screens/GetStartedPage';
import SelectionPage from './Screens/SelectionPage';
import InputPage from './Screens/InputPage';
import OutputPage from './Screens/OutputPage';

import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
        <Stack.Navigator>
            <Stack.Screen name="Get Started" component={GetStartedPage} options={{ headerShown: false }}/>
            <Stack.Screen name="SelectionPage" component={SelectionPage} options={{ headerShown: false }}/>
            <Stack.Screen name="InputPage" component={InputPage} options={{ headerShown: true, headerTitle: "Enter Your Details" }}/>
            <Stack.Screen name="OutputPage" component={OutputPage} options={{ headerShown: true, headerTitle: "Results" }}/>
        </Stack.Navigator>
    </NavigationContainer>
  );
}
