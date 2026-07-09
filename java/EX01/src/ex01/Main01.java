package ex01;

class Prodect{
	private String name; //상품명
	private int price; //가격
	
	public String getName() { //get~:값을 가져옴
		return name;
	}
	public void setName(String name) { //set~:값을 변경
		this.name = name;
	}
	
	public int getPrice() {
		return price;
	}
	public void setPrice(int price) {
		this.price = price;
	}
	
	
	
}

public class Main01 {
	public static void main(String[] args) {
		Prodect p = new Prodect();
		
		p.setName("컴퓨터");
		p.setPrice(3000000);
		
		p.setPrice(5500000);
		
		System.out.println(p.getName());
		System.out.println(p.getPrice());
	}
}
