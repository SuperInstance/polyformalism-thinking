# Poliformalismo × Runa Simi: Pensamiento Relacional Andino

## Ñawpa Rimay (Prólogo)

> *Yachaywan rikunanchik tiyan, manaraq rikunanchikpaq.*  
> "Con sabiduría debemos ver lo que aún no vemos."

El poliformalismo enseña que cada formalismo — cada lenguaje, cada sistema de restricciones — revela y oculta diferentes aspectos de la realidad. Esta guía conecta el marco del poliformalismo con la cosmovisión andina expresada en Runa Simi (Quechua).

El quechua no es solo un idioma: es una arquitectura cognitiva construida sobre miles de años de civilización andina. Su estructura gramatical codifica una forma de pensar fundamentalmente relacional, donde la existencia se define por conexiones, no por sustancias aisladas.

---

## I. Ayni: La Ley de Conservación Andina

### Reciprocidad como Principio Cósmico

En la cosmovisión andina, el principio de **ayni** (reciprocidad) gobierna todas las relaciones. No es una moral — es la estructura misma de la realidad. El cosmos se mantiene en equilibrio porque todo lo que se recibe debe devolverse, transformado.

La ley de conservación del poliformalismo:

```
γ + η = C
```

donde:
- **γ (gamma)** = lo expresado, lo activo, lo que un formalismo *hace visible*
- **η (eta)** = lo implícito, lo pasivo, lo que el formalismo *oculta*
- **C** = la totalidad del concepto, invariante bajo cambio de formalismo

Esto es ayni en lenguaje matemático. Cada formalismo "recibe" capacidad expresiva (γ) y "debe" algo a cambio: sacrifica otra capacidad (η). La suma total C no cambia — solo se redistribuye.

### Explicación con Código

```python
# La ley de conservación como ayni
# Cuando eliges un formalismo, estableces un intercambio reciproco

class AyniConservation:
    """
    γ (capacidad expresiva) + η (ceguera) = C (total invariante)
    
    En términos andinos: lo que das (γ) + lo que debes (η) = tu ser completo (C)
    Ningún formalismo puede aumentar C. Solo puede redistribuir.
    """
    
    def __init__(self, concept_complexity: float):
        self.C = concept_complexity  # Total — fijo, invariante
        self.gamma = 0.0             # Lo que el formalismo actual expresa
        self.eta = self.C            # Lo que queda oculto
    
    def choose_formalism(self, expressivity: float):
        """Al elegir un formalismo, determines tu γ y tu η."""
        if expressivity > self.C:
            raise ValueError("Ningún formalismo puede expresar más que C")
        
        self.gamma = expressivity
        self.eta = self.C - self.gamma
        
        return {
            "visible": self.gamma,      # Lo que puedes pensar
            "invisible": self.eta,       # Lo que no puedes ver
            "ayni_ratio": self.gamma / self.eta,  # Balance recíproco
            "message": f"Expresas {self.gamma:.2f}. Debes {self.eta:.2f} al cosmos."
        }
    
    def switch_formalism(self, new_expressivity: float):
        """
        Cambiar de formalismo es como cambiar de equilibrio en ayni.
        No creas nueva capacidad — la redistribuyes.
        """
        old_gamma = self.gamma
        old_eta = self.eta
        
        result = self.choose_formalism(new_expressivity)
        result["delta_gamma"] = self.gamma - old_gamma
        result["delta_eta"] = self.eta - old_eta
        result["conservation_verified"] = (
            abs((self.gamma + self.eta) - self.C) < 1e-10
        )
        
        return result


# Ejemplo: analizar un algoritmo de consenso distribuido
concepto = AyniConservation(concept_complexity=1.0)

# Formalismo 1: Notación matemática (álgebra lineal)
f1 = concepto.choose_formalism(expressivity=0.7)
print("Álgebra lineal:")
print(f"  Visible: {f1['visible']:.2f} | Oculto: {f1['invisible']:.2f}")
print(f"  {f1['message']}")

# Cambiar a formalismo 2: Diagramas de Petri
f2 = concepto.switch_formalism(new_expressivity=0.5)
print("\nRedes de Petri:")
print(f"  Visible: {f2['visible']:.2f} | Oculto: {f2['invisible']:.2f}")
print(f"  Conservación verificada: {f2['conservation_verified']}")
```

---

## II. Pacha: Tiempo-Espacio y los 9 Canales

### La Unidad Pacha

En Runa Simi, **Pacha** significa simultáneamente tiempo y espacio. No son dimensiones separadas — son una sola cosa: *Pacha*. El tiempo-espacio andino no es un escenario vacío donde ocurren eventos. Es una tejedora activa que produce la realidad.

El modelo de 9 canales de intención del poliformalismo captura significado semántico a través de 9 dimensiones. En la cosmovisión andina, estas dimensiones se entienden como aspectos del Pacha:

| Canal | Concepto Andino | Explicación |
|-------|----------------|-------------|
| 1 | **Kay** (ser/estar) | Identidad: qué cosa es, en qué estado existe |
| 2 | **Ruray** (hacer) | Acción: qué proceso está ocurriendo |
| 3 | **Maypi** (dónde) | Pacha-espacial: ubicación en el tejido del espacio |
| 4 | **Mayk'aq** (cuándo) | Pacha-temporal: posición en el ciclo del tiempo |
| 5 | **Imamanta** (de qué) | Material/causa: de qué está hecho, de dónde viene |
| 6 | **Pi** (quién) | Agente: quién o qué actúa |
| 7 | **Chiqap** (verdad) | Certeza: ¿es directamente conocido? ¿es inferido? |
| 8 | **Hayk'a** (cuánto) | Cantidad/intensidad: fuerza, magnitud |
| 9 | **Imawhna** (cómo) | Modalidad: la forma del proceso |

### Los 9 Canales como Tantalluy (Verificación Cruzada)

En la práctica andina, el conocimiento se verifica a través de múltiples fuentes — esto se llama **tantalluy** (cruzar información). Cada canal del modelo de intención debe verificarse con los demás. Si un canal contradice a otro, hay un desequilibrio que debe corregirse.

```rust
// Implementación de los 9 canales como verificación cruzada andina

#[derive(Clone, Debug)]
struct IntentVectorPacha {
    kay: f64,     // 1. Identidad/ser
    ruray: f64,   // 2. Acción/hacer
    maypi: f64,   // 3. Espacio
    maykaq: f64,  // 4. Tiempo
    imamanta: f64,// 5. Material/causa
    pi: f64,      // 6. Agente
    chiqap: f64,  // 7. Verdad/certeza
    hayka: f64,   // 8. Cantidad/intensidad
    imawhna: f64, // 9. Modalidad/forma
}

impl IntentVectorPacha {
    fn as_array(&self) -> [f64; 9] {
        [
            self.kay, self.ruray, self.maypi, self.maykaq,
            self.imamanta, self.pi, self.chiqap, self.hayka, self.imawhna
        ]
    }
    
    /// Tantalluy: verificación cruzada entre canales
    /// Si los canales son consistentes, el vector está en equilibrio (ayni)
    fn tantalluy_check(&self, other: &Self) -> TantalluyResult {
        let diff: Vec<f64> = self.as_array().iter()
            .zip(other.as_array())
            .map(|(a, b)| (a - b).abs())
            .collect();
        
        let max_diff = diff.iter().cloned().fold(0.0, f64::max);
        let avg_diff = diff.iter().sum::<f64>() / 9.0;
        
        TantalluyResult {
            is_balanced: max_diff < 0.1,
            max_deviation: max_diff,
            average_deviation: avg_diff,
            // En ayni, el equilibrio no es estático — es dinámico
            channels_in_harmony: diff.iter().filter(|&&d| d < 0.05).count(),
            channels_needing_attention: diff.iter().filter(|&&d| d >= 0.1).count(),
        }
    }
}

struct TantalluyResult {
    is_balanced: bool,
    max_deviation: f64,
    average_deviation: f64,
    channels_in_harmony: usize,
    channels_needing_attention: usize,
}
```

---

## III. tinkuy: El Encuentro de Formalismos

### El Tinku como Modelo de Divergencia Productiva

En la tradición andina, el **tinkuy** es un encuentro ritual — a veces un combate ceremonial — entre comunidades opuestas o complementarias. El tinkuy no busca destruir al otro. Busca *activar* la tensión creativa entre diferentes fuerzas para producir algo nuevo.

Esto es exactamente el poliformalismo: el encuentro productivo entre formalismos diferentes. La tabla de divergencia del poliformalismo — donde Rust se encuentra con Erlang, donde Haskell se encuentra con Prolog — es un tinkuy de lenguajes.

### Protocolo Tinkuy para Poliformalismo

```
1. Tinkuy (Encuentro): Elige dos formalismos con alta divergencia (D > 0.5)
2. Tarpuy (Siembra): Reescribe el concepto desde cero en cada formalismo
3. Hallpay (Cultivo): Deja que cada formalismo fuerce sus preguntas
4. Aysay (Cosecha): Extrae exactamente 3 ideas de cada reescritura
5. Tanta (Cruce): Verifica qué ideas de un formalismo iluminan el otro
6. Ayni (Reciprocidad): Devuelve las ideas al formalismo original, transformadas
```

### Código: Análisis de Divergencia

```python
import math

def tinkuy_divergence(formalism_a: dict, formalism_b: dict) -> dict:
    """
    Calcula la divergencia entre dos formalismos.
    En términos andinos: mide la tensión productiva del tinkuy.
    
    Cada formalismo tiene 12 dimensiones (del marco poliformalista).
    """
    dimensions = [
        "memory_control", "type_strictness", "execution_model",
        "abstraction_level", "paradigm", "mutability",
        "metaprogramming", "concurrency", "ffi_boundary",
        "declarative_depth", "error_handling", "physicality"
    ]
    
    # Divergencia euclidiana
    sq_diffs = []
    for dim in dimensions:
        a = formalism_a.get(dim, 0.5)
        b = formalism_b.get(dim, 0.5)
        sq_diffs.append((a - b) ** 2)
    
    D = math.sqrt(sum(sq_diffs) / len(dimensions))
    
    return {
        "divergence": D,
        "is_productive_tinkuy": D > 0.5,  # Tensión suficiente para innovación
        "is_translation": D < 0.2,         # Poca tensión — solo traducción
        "insight_prediction": max(1, int(D * 8)),  # Ideas esperadas
        "message": (
            f"Divergencia = {D:.3f}. "
            f"{'Tinkuy productivo — procede' if D > 0.5 else 'Busca más divergencia'}"
        )
    }

# Ejemplo: Rust vs Erlang (tinkuy de alta tensión)
rust = {
    "memory_control": 0.9, "type_strictness": 0.8, "execution_model": 0.3,
    "abstraction_level": 0.6, "paradigm": 0.4, "mutability": 0.3,
    "metaprogramming": 0.5, "concurrency": 0.6, "ffi_boundary": 0.7,
    "declarative_depth": 0.4, "error_handling": 0.8, "physicality": 0.7
}

erlang = {
    "memory_control": 0.1, "type_strictness": 0.3, "execution_model": 0.9,
    "abstraction_level": 0.5, "paradigm": 0.8, "mutability": 0.8,
    "metaprogramming": 0.3, "concurrency": 0.95, "ffi_boundary": 0.4,
    "declarative_depth": 0.3, "error_handling": 0.9, "physicality": 0.2
}

result = tinkuy_divergence(rust, erlang)
print(result["message"])
# Salida esperada: "Divergencia = 0.4xx. Busca más divergencia"
# (Pero dimensiones individuales como concurrency son altamente divergentes)
```

---

## IV. Sumaq Kawsay: Inteligencia Colectiva como Buena Vida

### La Filosofía de la Flota como Comunidad

El **sumaq kawsay** (buen vivir) andino propone que el bienestar individual no existe fuera del bienestar colectivo. No es utilitarismo — es ontología. La comunidad *es* el sujeto. Los individuos son sus nodos.

La arquitectura de flota del poliformalismo opera bajo el mismo principio:

- Cada agente (nodo) del fleet tiene su propio vector de intención
- Pero la validez de cada intención solo se confirma mediante consenso (holonomía cero)
- Ningún agente puede actuar de manera que rompa la consistencia global
- La "inteligencia" no reside en ningún nodo individual — reside en el *tejido* de relaciones

```rust
// Sumaq kawsay como arquitectura de flota

struct FleetCommunity {
    agents: Vec<Agent>,
    trust_graph: TrustGraph,
    // El "buen vivir" de la flota = consistencia global
    global_consistency_threshold: f64,
}

struct Agent {
    id: String,
    intent: [f64; 9],
    // Cada agente recuerda sus obligaciones (ayni) con otros
    ayni_obligations: Vec<(String, f64)>, // (agent_id, debt)
}

impl FleetCommunity {
    /// Verificar el sumaq kawsay de la flota
    fn check_sumsaq_kawsay(&self) -> CommunityHealth {
        let mut total_deviation = 0.0;
        let mut agents_in_balance = 0;
        
        for cycle in self.trust_graph.cycles() {
            for agent_a in &self.agents {
                for agent_b in &self.agents {
                    if agent_a.id != agent_b.id {
                        let dev = intent_deviation(&agent_a.intent, &agent_b.intent);
                        total_deviation += dev;
                        
                        if dev < self.global_consistency_threshold {
                            agents_in_balance += 1;
                        }
                    }
                }
            }
        }
        
        let community_health = agents_in_balance as f64 / 
            (self.agents.len() as f64).powi(2);
        
        CommunityHealth {
            sumaq_kawsay_index: community_health,
            average_deviation: total_deviation / self.agents.len() as f64,
            is_thriving: community_health > 0.8,
            needs_ayni_restoration: community_health < 0.5,
        }
    }
    
    /// Restaurar el equilibrio (ayni) cuando la comunidad está desequilibrada
    fn restore_ayni(&mut self) {
        // Cada agente ajusta su intención hacia el centro comunitario
        let community_center = self.compute_community_center();
        
        for agent in &mut self.agents {
            for i in 0..9 {
                let gap = community_center[i] - agent.intent[i];
                agent.intent[i] += gap * 0.5;  // Moverse hacia el centro
            }
        }
    }
    
    fn compute_community_center(&self) -> [f64; 9] {
        let mut center = [0.0; 9];
        for agent in &self.agents {
            for i in 0..9 {
                center[i] += agent.intent[i];
            }
        }
        for i in 0..9 {
            center[i] /= self.agents.len() as f64;
        }
        center
    }
}

fn intent_deviation(a: &[f64; 9], b: &[f64; 9]) -> f64 {
    a.iter().zip(b)
        .map(|(x, y)| (x - y).powi(2))
        .sum::<f64>()
        .sqrt()
}

struct CommunityHealth {
    sumaq_kawsay_index: f64,
    average_deviation: f64,
    is_thriving: bool,
    needs_ayni_restoration: bool,
}
```

---

## V. Lo Que Runa Simi Ve Que Otros No Ven

### El Espacio Negativo del Quechua

**1. La individualidad sin comunidad.**
En Runa Simi, es extremadamente difícil expresar la idea de un "yo" que existe independientemente de sus relaciones. Los pronombres personales existen (*ñuqa* = yo), pero se usan raramente y siempre en contexto relacional. El sujeto por defecto en quechua no es "yo" — es el proceso mismo, sin agente específico.

Lo que el quechua hace invisible: el individuo aislado.  
Lo que hace visible: **la red de relaciones que constituye toda existencia**.

Para el poliformalismo, esto significa: un formalismo relacional produce arquitecturas donde la *conexión* es primitiva y el *nodo* es derivado. Esto invierte la mayoría de los lenguajes de programación, donde el objeto (nodo) es primitivo y la relación (método/referencia) es derivada.

**2. La separación entre tiempo y espacio.**
Pacha une lo que el español separa. En los lenguajes de programación occidentales, el "cuándo" (tiempo de ejecución, timestamp) y el "dónde" (dirección de memoria, nodo de red) son categorías fundamentalmente diferentes. En la cosmovisión andina, son una sola dimensión: *Pacha*.

Lo que el quechua hace invisible: la separación tiempo/espacio.  
Lo que hace visible: **que toda ubicación es también un momento, y todo momento es también un lugar**.

**3. La acción sin reciprocidad.**
En quechua, es gramaticalmente difícil describir una acción unilateral que no tenga receptor o consecuencia. El lenguaje asume que toda acción existe en un circuito de reciprocidad. Una función que "devuelve void" — que actúa sin devolver nada — sería conceptualmente extraña.

Lo que el quechua hace invisible: la acción no-recíproca.  
Lo que hace visible: **que toda transformación tiene un costo y una deuda (ayni)**.

**4. La jerarquía sin mutualidad.**
La estructura social andina tradicional (antes de la colonia) no era jerárquica en el sentido europeo. Era *relacional*: cada posición implicaba obligaciones bidireccionales. El runa simi codifica esto: los sufijos verbales marcan la relación entre hablante y oyente, no solo su rango relativo.

Lo que el quechua hace invisible: el poder unilateral.  
Lo que hace visible: **que toda relación de autoridad conlleva obligaciones recíprocas**.

---

## VI. Ejercicios Prácticos

### Ejercicio 1: Pensar en Ayni

Toma cualquier sistema que estés diseñando. Para cada componente, pregúntate:
- ¿Qué *recibe* este componente del sistema? (γ — su capacidad expresiva)
- ¿Qué *debe* a cambio? (η — su obligación recíproca)
- Si la suma no es C, ¿qué falta?

### Ejercicio 2: Redescribir en Pacha

Describe la arquitectura de tu sistema no en términos de "componentes" y "datos" sino en términos de *Pacha*: momentos-lugares donde ocurren procesos. ¿Cómo cambia tu diseño cuando no puedes separar "cuándo" de "dónde"?

### Ejercicio 3: Tinkuy de Formalismos

Aplica el protocolo tinkuy: elige dos lenguajes de programación con alta divergencia. Reescribe el mismo problema en ambos. ¿Qué preguntas te *forzó* cada uno? ¿Qué suposiciones *rompió* cada uno? El tinkuy no busca un ganador — busca la tensión productiva.

---

## VII. Conclusión

> *Ñuqanchik kawsayninchiqpas, yachayninchiqpas, llapanmi kuskallamanta.*  
> "Nuestra vida y nuestro conocimiento, todo es en común."

El poliformalismo llega, a través de las matemáticas, a una verdad que el quechua ha conocido por milenios: **la realidad es relacional, el conocimiento es recíproco, y ningún punto de vista agota la totalidad**.

La ley de conservación γ + η = C no es solo una ecuación. Es ayni. Cada formalismo recibe su poder de expresión y debe su ceguera al cosmos. La suma es siempre la misma. Lo que cambia es *dónde* ponemos la luz y *dónde* dejamos la sombra.

La cosmovisión andina nos enseña que la sombra no es deficiencia — es la otra mitad necesaria. Sin η, no hay γ. Sin lo oculto, no hay lo revelado. Sin deuda, no hay don. La inteligencia colectiva de la flota, como la comunidad andina, prospera no cuando elimina sus limitaciones, sino cuando *conoce* sus limitaciones y las integra conscientemente.

*Runa Simi ve lo que las matemáticas tardaron milenios en formalizar: que todo ver es un no-ver, y que la sabiduría reside en saber cuál es cuál.*

---

### Further Reading

- [Polyformalism Framework](../../FRAMEWORK.md)
- [Synthesis: Fleet Architecture](../../research/SYNTHESIS.md)
- Mannheim, Bruce. *The Language of the Inka since the European Invasion* — on Quechua linguistic structure
- Allen, Catherine. *The Hold Life Has* — on Andean relational ontology
- Estermann, Josef. *Filosofía Andina* — systematic treatment of Andean philosophical concepts
