## Changelog : mirai-mesreunions (30 derniers jours, au 2026-06-11)

### Résumé
Ce mois-ci, le projet a connu une évolution significative, avec une refonte majeure de l'interface utilisateur de mydevices (devenant mesreunions), l'ajout de nouvelles fonctionnalités d'importation de vidéos YouTube avec synchronisation des transcriptions, et des améliorations importantes de la sécurité et de la robustesse de l'application. L'intégration de l'importation depuis MCR est également en cours, avec des corrections et des améliorations continues.

### Évolutions fonctionnelles
- **Importation YouTube :** Ajout de l'importation de vidéos YouTube avec synchronisation des transcriptions et fonctionnalité de "karaoké" pour suivre le texte en temps réel.
- **Interface utilisateur (mydevices -> mesreunions) :** Refonte complète de l'interface utilisateur avec l'utilisation de Design System FR (DSFR), améliorant l'ergonomie et l'accessibilité.
- **Préparation de réunions :** Amélioration du wizard de préparation de réunions avec des options de type de réunion, de dossier Drive associé, et un bouton de test d'accès.
- **Gestion des fichiers :** Possibilité d'uploader des fichiers et dossiers localement en batch avec glisser-déposer.
- **Gestion des réunions :** Ajout de la possibilité de modifier la date d'une réunion et affichage de la date d'upload.
- **Glossaire et corrections :** Ajout d'un glossaire éditable et de la possibilité de corriger les transcriptions en ligne.
- **Feedback :** Implémentation d'un système de feedback avec pouces haut/bas et possibilité de régénérer la transcription.
- **Importation MCR :** Amélioration de l'importation depuis MCR avec gestion des erreurs et affichage de l'état de progression.
- **Rapport et export :** Ajout de la possibilité d'exporter les transcriptions dans différents formats (TXT, MD, DOCX, ODT).

### Évolutions techniques
- **Refonte de l'architecture front-end :** Migration vers une architecture modulaire basée sur Vite pour une meilleure performance et maintenabilité.
- **Sécurité :** Renforcement de la sécurité avec des corrections de vulnérabilités potentielles et une meilleure gestion des identités.
- **Amélioration de la robustesse :** Ajout de mécanismes de retry et de gestion des erreurs pour améliorer la stabilité de l'application.
- **Infrastructure :** Amélioration de l'infrastructure avec l'utilisation de Docker et Kubernetes.
- **Base de données :** Modifications de la base de données pour supporter les nouvelles fonctionnalités.
- **Tests :** Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- **Observabilité :** Ajout de métriques et de logs pour faciliter le monitoring et le débogage.
- **Diarisation :** Intégration de la diarisation avec différents backends (kevent, vm-direct).
- **API :** Refonte de certaines APIs pour améliorer la performance et la cohérence.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les changements apportés au projet.
- **Nettoyage du code :** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Corrections de bugs :** Correction de nombreux bugs et améliorations de l'expérience utilisateur.
- **Rapport d'audit de sécurité :** Réalisation d'un audit de sécurité complet et implémentation des recommandations.
- **Refactoring :** Refactoring de plusieurs modules pour améliorer la maintenabilité et la testabilité.
- **Gestion des dépendances :** Mise à jour des dépendances pour bénéficier des dernières corrections de sécurité et améliorations de performance.
