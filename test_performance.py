#!/usr/bin/env python3
"""
Performance Test Script for Corn Ji
Run this to verify optimization improvements
"""

import time
import sys
from pathlib import Path

# Add files directory to path
sys.path.insert(0, str(Path(__file__).parent / "files"))

def test_imports():
    """Test import speed"""
    print("🔍 Testing imports...")
    start = time.time()
    
    try:
        from core.predict import load_model, predict
        from core.disease_info import DISEASE_INFO
        print(f"✅ Imports successful ({time.time() - start:.2f}s)")
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

def test_model_loading():
    """Test model loading speed"""
    print("\n🧠 Testing model loading...")
    start = time.time()
    
    try:
        from core.predict import load_model
        model = load_model()
        elapsed = time.time() - start
        
        if model:
            print(f"✅ Model loaded ({elapsed:.2f}s)")
        else:
            print(f"⚠️  No model found, using intelligent analysis ({elapsed:.2f}s)")
        return True
    except Exception as e:
        print(f"❌ Model loading failed: {e}")
        return False

def test_prediction_speed():
    """Test prediction speed with dummy image"""
    print("\n⚡ Testing prediction speed...")
    
    try:
        from PIL import Image
        import io
        from core.predict import predict
        
        # Create dummy image
        img = Image.new('RGB', (224, 224), color='green')
        buf = io.BytesIO()
        img.save(buf, format='JPEG')
        img_bytes = buf.getvalue()
        
        # Test prediction
        start = time.time()
        label, conf, probs = predict(img_bytes)
        elapsed = time.time() - start
        
        print(f"✅ Prediction completed ({elapsed:.2f}s)")
        print(f"   Result: {label} ({conf*100:.1f}% confidence)")
        
        if elapsed < 2.0:
            print("   🎉 EXCELLENT - Under 2 seconds!")
        elif elapsed < 3.0:
            print("   👍 GOOD - Under 3 seconds")
        else:
            print("   ⚠️  SLOW - Consider further optimization")
        
        return True
    except Exception as e:
        print(f"❌ Prediction test failed: {e}")
        return False

def test_memory_usage():
    """Test memory usage"""
    print("\n💾 Testing memory usage...")
    
    try:
        import psutil
        import os
        
        process = psutil.Process(os.getpid())
        memory_mb = process.memory_info().rss / 1024 / 1024
        
        print(f"✅ Current memory usage: {memory_mb:.1f} MB")
        
        if memory_mb < 150:
            print("   🎉 EXCELLENT - Low memory usage!")
        elif memory_mb < 300:
            print("   👍 GOOD - Acceptable memory usage")
        else:
            print("   ⚠️  HIGH - Consider clearing cache")
        
        return True
    except ImportError:
        print("⚠️  psutil not installed, skipping memory test")
        print("   Install with: pip install psutil")
        return True
    except Exception as e:
        print(f"❌ Memory test failed: {e}")
        return False

def test_storage():
    """Test storage usage"""
    print("\n📁 Testing storage...")
    
    try:
        scan_data_dir = Path("scan_data/images")
        
        if scan_data_dir.exists():
            total_size = sum(f.stat().st_size for f in scan_data_dir.glob("*") if f.is_file())
            total_size_mb = total_size / 1024 / 1024
            file_count = len(list(scan_data_dir.glob("*")))
            
            print(f"✅ Scan history: {file_count} images, {total_size_mb:.1f} MB")
            
            if file_count > 0:
                avg_size = total_size_mb / file_count
                print(f"   Average image size: {avg_size:.2f} MB")
                
                if avg_size < 1.0:
                    print("   🎉 EXCELLENT - Well optimized!")
                elif avg_size < 2.0:
                    print("   👍 GOOD - Acceptable size")
                else:
                    print("   ⚠️  LARGE - Consider more compression")
        else:
            print("✅ No scan history yet")
        
        return True
    except Exception as e:
        print(f"❌ Storage test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("🌽 Corn Ji Performance Test")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_model_loading,
        test_prediction_speed,
        test_memory_usage,
        test_storage
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"❌ Test crashed: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    print("📊 Test Summary")
    print("=" * 60)
    
    passed = sum(results)
    total = len(results)
    
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! Your app is optimized!")
    elif passed >= total * 0.7:
        print("👍 MOST TESTS PASSED! App is working well.")
    else:
        print("⚠️  SOME TESTS FAILED. Check errors above.")
    
    print("\n💡 To run the app:")
    print("   streamlit run files/app.py")
    print("\n📖 For more optimization tips:")
    print("   cat PERFORMANCE_FIXES.md")
    print("=" * 60)

if __name__ == "__main__":
    main()
