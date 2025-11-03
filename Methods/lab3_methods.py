# Lab 3: GradeSystem Class
# -----------------------
# Yêu cầu:
# 1. Tạo class GradeSystem có method calculateGPA
# 2. Method này nhận danh sách điểm (0-100) và trả về GPA trung bình (thang 4.0)
# 3. Dựa theo quy đổi: A:90+, B:80+, C:70+, D:60+, F:<60

class GradeSystem:
    def calculateGPA(self, scores):
        def convert(score):
            if score >= 90: return 4.0
            elif score >= 80: return 3.0
            elif score >= 70: return 2.0
            elif score >= 60: return 1.0
            else: return 0.0

        gpas = [convert(s) for s in scores]
        return round(sum(gpas) / len(gpas), 2)

# Test
if __name__ == "__main__":
    system = GradeSystem()
    scores = [95, 82, 76, 64, 58]
    print("GPA:", system.calculateGPA(scores))
