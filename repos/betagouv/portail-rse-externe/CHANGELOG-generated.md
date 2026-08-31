## Changelog : portail-rse-externe (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois a été marqué par une évolution majeure de l'architecture pour intégrer la deuxième version (v2) du moteur d'intelligence artificielle. Le projet prépare ainsi une transition fluide entre l'ancienne et la nouvelle version de l'analyse, tout en améliorant la robustesse du système et la clarté de la documentation pour les déploiements.

### Évolutions fonctionnelles
- **Amélioration de l'expérience utilisateur** : Mise en place de messages d'erreur génériques pour une communication plus claire avec l'utilisateur.
- **Correction de bug** : Résolution d'un problème qui interrompait le traitement lorsque le système rencontrait un fichier PDF vide.

### Évolutions techniques
- **Intégration de l'IA v2** : Mise en œuvre du nouveau moteur d'intelligence artificielle, incluant la création de nouveaux points d'entrée et la gestion de requêtes sur des URLs distinctes pour la v1 et la v2.
- **Refactorisation de l'architecture** :
    - Séparation de l'analyse IA v1 dans un répertoire dédié pour permettre la coexistence des versions.
    - Extraction de la logique de notification vers un module commun partagé entre la v1 et la v2.
- **Qualité logicielle et tests** :
    - Amélioration de la couverture de tests pour le framework Flask.
    - Intégration de `pytest` pour l'exécution automatisée des tests.
- **Infrastructure** : Mise à jour de la version du conteneur Flask.

### Autres changements
- **Documentation** :
    - Centralisation de la documentation dans un répertoire dédié.
    - Ajout de précisions techniques sur l'utilisation de Podman, les variables d'environnement nécessaires à la v2 et les chemins de production.
    - Mise à jour des commandes de déploiement.
- **Maintenance** : Nettoyage du code (suppression d'imports inutilisés et de commandes obsolètes).
