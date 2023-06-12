import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class ToyShopLottery {
    private List<Toy> toys = new ArrayList<>();

    public void addToy(Toy toy) {
        toys.add(toy);
    }

    public Toy getRandomToy(int maxWeight) {
        List<Toy> validToys = new ArrayList<>();
        for (Toy toy : toys) {
            if (toy.getWeight() <= maxWeight) {
                validToys.add(toy);
            }
        }
        if (validToys.isEmpty()) {
            return null;
        }
        int randomIndex = new Random().nextInt(validToys.size());
        return validToys.get(randomIndex);
    }
}

class Toy {
    private String name;
    private int weight;

    public Toy(String name, int weight) {
        this.name = name;
        this.weight = weight;
    }

    public int getWeight() {
        return weight;
    }
}
