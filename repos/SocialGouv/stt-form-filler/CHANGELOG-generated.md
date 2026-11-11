## Changelog : stt-form-filler (30 derniers jours, au 10 novembre 2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes importantes en termes de performance et de fiabilité. L'outil de remplissage vocal du formulaire MDPH bénéficie d'une interface utilisateur plus intuitive et de réglages plus précis. Parallèlement, une refonte majeure de l'infrastructure technique permet désormais une synthèse vocale beaucoup plus rapide et un déploiement automatisé et sécurisé.

### Évolutions fonctionnelles
- **Amélioration de l'interface utilisateur (UI/UX) :**
    - Refonte de l'écran d'accueil « Avant de commencer ».
    - Ajout d'un menu latéral permettant de visualiser et naviguer entre les questions d'une même étape.
    - Intégration des réglages de la voix directement dans l'en-tête de la page.
    - Amélioration de l'indicateur d'étapes pour une meilleure visibilité du progrès.
- **Ergonomie et accessibilité :**
    - Ajout du support de la barre d'espace pour déclencher la parole.
- **Corrections :**
    - Correction de la gestion des montants financiers pour conserver la précision des centimes (au lieu d'un arrondi à l'euro).

### Évolutions techniques
- **Optimisation des performances :**
    - Accélération massive de la synthèse vocale (Piper) : le temps de génération d'une phrase est passé de 2,7 s à 0,3 s grâce à une gestion optimisée des ressources CPU.
    - Garantie d'une allocation de ressources CPU minimale pour éviter les ralentissements lors de la synthèse.
- **Infrastructure et CI/CD :**
    - Refonte complète du pipeline de déploiement : la construction des images Docker est désormais automatisée via GitHub Actions directement dans le cluster OVH.
    - Sécurisation du processus de déploiement via l'utilisation de secrets scellés (kubeseal) et de jetons dédiés pour les dépôts privés.
    - Mise en place d'un environnement de développement robuste sur la "fabrique" avec des sondes de santé (/healthz).
- **Architecture logicielle :**
    - Généralisation du support des modèles de langage (LLM) : l'application peut désormais utiliser n'importe quelle API compatible avec le standard OpenAI.

### Autres changements
- **Documentation :** Mise à jour de la documentation incluant le fil d'Ariane, les pages légales et le détail des questions de suivi.
