## Changelog : n8n-nodes-s3-presigner (30 derniers jours, au 21 octobre 2026)

### Résumé
Ce mois a été marqué par le lancement officiel et la structuration du projet. Les évolutions majeures permettent désormais d'utiliser le nœud avec n'importe quel service de stockage compatible S3 (et pas seulement AWS) et améliorent la fiabilité de l'envoi de fichiers grâce à une meilleure gestion automatique des types de contenu.

### Évolutions fonctionnelles
- **Compatibilité étendue** : Support désormais disponible pour AWS ainsi que pour tous les services de stockage compatibles avec le protocole S3.
- **Amélioration de l'upload** : Gestion automatique de l'en-tête `Content-Type` lors de la génération d'URLs pré-signées pour les opérations de téléchargement (Put), garantissant une meilleure reconnaissance des fichiers.
- **Optimisation de l'interface** : Mise à jour des valeurs par défaut et des indicateurs (placeholders) pour le type de contenu des fichiers afin de faciliter la configuration par l'utilisateur.

### Évolutions techniques
- **Automatisation CI/CD** : Mise en place complète de la chaîne d'intégration et de déploiement continus.
- **Optimisation du déploiement** : Refonte du workflow de déploiement continu (CD) pour s'appuyer directement sur les artefacts générés lors de l'étape d'intégration (CI).
- **Initialisation du projet** : Création de la structure initiale du dépôt sous son nouveau nom.

### Autres changements
- **Qualité du code** : Ajout de scripts de build et de linting pour assurer la conformité et la propreté du code.
- **Documentation** : Mise à jour du fichier README.
