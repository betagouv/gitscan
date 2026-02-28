## Changelog : docs (30 derniers jours)

### Résumé
Les 30 derniers jours ont été marqués par des améliorations significatives en matière d'intelligence artificielle, avec l'intégration de nouvelles fonctionnalités et l'optimisation de l'expérience utilisateur. Des corrections de sécurité ont également été apportées, ainsi que des améliorations de l'interface et de l'accessibilité. Des efforts ont été déployés pour améliorer la gestion des utilisateurs et l'onboarding.

### Évolutions fonctionnelles
- Ajout d'un modal de demande d'accès lors du déplacement de documents (#1886).
- Intégration de la nouvelle fonctionnalité Blocknote AI, avec un indicateur d'état accessible (#1016, #1922).
- Possibilité de dupliquer les sous-pages (#1893).
- Ajout de documentation pour l'onboarding des nouveaux utilisateurs (#1891).
- Ajout de paramètres UTM aux liens de partage de documents (#1876).
- Ajout d'une barre flottante avec un bouton de réduction pour le panneau latéral (#1876).
- Possibilité d'imprimer un document directement depuis le navigateur (#1832).
- Gestion des demandes de réconciliation pour les comptes utilisateurs (#1878).
- Ajout d'un support pour la signature AWS S3 avec la variable d'environnement `AWS_S3_SIGNATURE_VERSION` (#1909).

### Évolutions techniques
- Utilisation de `uvicorn` pour servir le backend, améliorant potentiellement les performances (#1906).
- Refonte de la gestion du streaming avec le service d'IA (#1906).
- Utilisation de pydantic pour gérer le protocole de flux de données Vercel pour l'IA (#1906).
- Ajout de support pour l'architecture ARM64 dans les builds Docker (#1851).
- Optimisation du workflow Docker Hub (#1919).
- Mise à jour des dépendances frontend pour être compatibles avec ESLint v10 (#1913).
- Configuration personnalisée de la cache (#1905).
- Correction de l'ordre de priorité des sondes liveness et readiness dans le déploiement Helm (#1849).
- Utilisation des ressources Celery au lieu de celles du backend dans le déploiement Helm (#1848).
- Ajout de tests Trivy pour l'image backend (#1909).
- Activation de la vérification Trivy sur l'image backend (#1909).

### Autres changements
- Corrections de vulnérabilités de sécurité (CVE) (#1915, #1903, #1806).
- Amélioration de l'accessibilité : prévention de la focalisation sur les dates (#1855), amélioration de la focalisation après la navigation (#1854).
- Alignement des couleurs avec la nouvelle charte graphique Figma (#1869).
- Amélioration du système de remplacement de thèmes par configuration (#1869).
- Ajout de tests de régression pour l'exportation PDF (#1762).
- Ajout d'un fichier `.trivyignore` pour ignorer certaines vulnérabilités (#1915).
- Mise à jour des chaînes de traduction (#1925).
- Remplacement du lien de démonstration dans le README (#1875).
- Correction de l'affichage du timestamp des documents (#1902).
- Correction d'un bug lié à la synchronisation du store broadcast (#1846).
- Correction d'un problème d'espacement des blocs callout pour les anciens navigateurs (#1914).
- Correction d'un bug lié à l'utilisation de la taille maximale des fichiers de conversion (#1913).
- Suppression du code lié à l'ancien système de templates (#1780).
- Suppression des paramètres d'IA obsolètes (#1905).
- Ajout de la possibilité de configurer le bot IA frontend (#1906).
- Durcissement de la sécurité du proxy IA backend (#1906).
- Ajout d'un proxy IA backend (#1906).
- Suppression de l'affichage du contenu des documents lors de la récupération sans contenu (#1910).
- Ajout d'annonces d'état de l'IA avec aria-live (#1906).
- Correction d'un bug dans le workflow CI pour les forks (#1851).
- Correction d'un bug dans le Dockerfile pour l'utilisateur du hub (#1828).
- Mise à jour de la dépendance axios vers la version 1.13.5 (correction de sécurité) (#1903).
