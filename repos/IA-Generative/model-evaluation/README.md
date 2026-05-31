# README – Évaluation de Modèles LLM  

## 📘 Présentation  

Ce dépôt a pour ambition de fournir un cadre complet pour **évaluer des modèles de langage**.  
Il regroupe :  

- **Jeux d’évaluation** (datasets) prêts à l’emploi.  
- **Outillage** d’évaluation, notamment l’intégration de **[Promptfoo](https://www.promptfoo.dev/)** pour la création, l’exécution et le suivi de scénarios de tests automatisés.  

Le projet vise à simplifier la mise en place d’un processus d’évaluation reproductible et extensible, adapté aux besoins des équipes du Ministère de l’Intérieur et de l’administration territoriale de l’État (ATE).

---

## 🚀 Démarrage rapide  

### Prérequis  

| Prérequis | Version minimale |
|-----------|------------------|
| Node.js   | 18.x |
| npm / yarn| 9.x |
| Python    | 3.9 (si vous utilisez les scripts Python) |
| Docker (optionnel) | 20.10.x |

### Installation  

```bash
# 1. Cloner le dépôt
git clone https://github.com/your-org/model-evaluation.git
cd model-evaluation

# 2. Installer les dépendances Node
npm install   # ou `yarn install`

# 3. Installer les dépendances Python (optionnel)
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Configuration de Promptfoo  

```bash
# Installer Promptfoo globalement (ou en tant que dépendance du projet)
npm install -g @promptfoo/cli

# Vérifier l’installation
promptfoo --version
```

---

## 📊 Jeux d’évaluation  

Le répertoire `datasets/` contient plusieurs jeux de tests :  

| Nom du dataset | Description | Format |
|----------------|-------------|--------|
| `qa_french.json` | Questions‑réponses en français (exemple : administration publique) | JSONL |
| `summarization.csv` | Paires texte / résumé pour évaluer la capacité de synthèse | CSV |
| `bias_test.yaml` | Scénarios ciblant les biais de sensibilité | YAML |

> **Note** : chaque jeu est accompagné d’un fichier `README.md` détaillant la provenance, la licence et les instructions d’utilisation.

---

## 🛠️ Utilisation de Promptfoo  

Promptfoo permet de **décrire, exécuter et comparer** des scénarios de prompts.  

Exemple de fichier de configuration (`promptfoo.config.js`) :

```js
module.exports = {
  prompts: [
    {
      name: "QA Français",
      description: "Évaluation de la pertinence des réponses en français.",
      provider: "openai",
      model: "gpt-4o-mini",
      dataset: "datasets/qa_french.json",
      evaluator: "accuracy",
    },
    // …autres scénarios
  ],
};
```

Lancer les tests :

```bash
promptfoo run
```

Les résultats sont générés sous forme de rapports HTML et JSON dans le dossier `reports/`.

---

## 🤝 Contribuer  

Les contributions sont les bienvenues !  

- **Issues** – Signalez bugs, proposez des améliorations ou discutez de nouvelles idées.  
- **Pull Requests** – Soumettez vos ajouts (nouveaux jeux de données, meilleures métriques, scripts d’automatisation, etc.).  

> Veuillez respecter les bonnes pratiques suivantes :  
> 1. Créez une branche dédiée (`feature/nom-de-la-fonction`).  
> 2. Ajoutez des tests unitaires et/ou d’intégration lorsque cela est pertinent.  
> 3. Mettez à jour la documentation (README, commentaires, etc.).  
> 4. Soumettez la PR en utilisant les **templates** fournis dans le répertoire `.github/`.  

Toutes les contributions seront revues dans les plus brefs délais.

---

## 📄 Licence  

Ce projet est publié sous licence **Apache 2.0**. Consultez le fichier `LICENSE` pour plus de détails.

---

## 📞 Contact  

- **Mainteneur principal** : [Fabrique Numérique Ministère de l'Intérieur]  
- **Canal de discussion** : Utilisez les **Discussions GitHub** du dépôt pour poser des questions ou proposer des idées.  

---

> **Rappel** : L’utilisateur reste responsable de la vérification finale et de l’usage des contenus générés. Cette solution doit être employée conformément aux règles de l'Etat et aux exigences du RGPD.
