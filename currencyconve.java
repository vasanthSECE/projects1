import java.util.Scanner;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import org.json.JSONObject;

public class CurrencyConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Step 1: Currency Selection
        System.out.println("Currency Selection:");
        System.out.print("Enter the base currency code (e.g., USD, EUR): ");
        String baseCurrency = scanner.next();
        System.out.print("Enter the target currency code (e.g., USD, EUR): ");
        String targetCurrency = scanner.next();

        // Step 2: Fetch Currency Rates
        double exchangeRate = getExchangeRate(baseCurrency, targetCurrency);

        if (exchangeRate == -1) {
            System.out.println("Failed to fetch currency rates. Please try again later.");
            return;
        }

        // Step 3: Amount Input
        System.out.print("Enter the amount you want to convert: ");
        double amount = scanner.nextDouble();

        // Step 4: Currency Conversion
        double convertedAmount = amount * exchangeRate;

        // Step 5: Display Result
        System.out.println("\nConverted Amount: " + convertedAmount + " " + targetCurrency);

        scanner.close();
    }

    // Method to fetch exchange rates from an API
    public static double getExchangeRate(String baseCurrency, String targetCurrency) {
        try {
            URL url = new URL("https://api.exchangeratesapi.io/latest?base=" + baseCurrency + "&symbols=" + targetCurrency);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");

            BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            StringBuilder response = new StringBuilder();
            String line;

            while ((line = reader.readLine()) != null) {
                response.append(line);
            }

            reader.close();

            JSONObject jsonResponse = new JSONObject(response.toString());

            if (!jsonResponse.has("rates")) {
                return -1;
            }

            JSONObject rates = jsonResponse.getJSONObject("rates");

            if (!rates.has(targetCurrency)) {
                return -1;
            }

            return rates.getDouble(targetCurrency);
        } catch (Exception e) {
            e.printStackTrace();
            return -1;
        }
    }
}
