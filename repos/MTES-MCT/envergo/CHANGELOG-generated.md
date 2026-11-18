## Changelog : envergo (30 derniers jours, au 17 novembre 2026)

### Résumé
Ce mois a été marqué par une montée en puissance de la sécurité et de la robustesse de la plateforme. Les utilisateurs bénéficieront d'une meilleure visibilité sur les détails des projets et d'une interface plus fluide. Côté technique, le projet a franchi des étapes importantes avec la mise à jour de ses composants majeurs (Django, PostgreSQL) et l'automatisation de la surveillance des vulnérabilités.

### Évolutions fonctionnelles
- **Gestion des Avis & Dossiers** : Amélioration de l'affichage des détails des projets sur les pages d'avis réglementaires, avec la possibilité de réduire les sections pour plus de clarté [#1345](https://github.com/MTES-MCT/envergo/pull/1345). Ajout de la possibilité de créer un avis directement sans passer par une demande existante.
- **Notifications & Communication** : Amélioration des liens de notification Tchap vers le tableau de bord, ajout d'alertes pour les nouveaux dossiers [#1368](https://github.com/MTES-MCT/envergo/pull/1368) et mise en place d'un outil facilitant l'envoi manuel d'e-mails de notification [#1344](https://github.com/MTES-MCT/envergo/pull/1344).
- **Interface Utilisateur (UI) & Accessibilité** : Refonte visuelle des étiquettes (tags) [#1377](https://github.com/MTES-MCT/envergo/pull/1377), passage du système d'accordéon vers un format "concertina" [#1391](https://github.com/MTES-MCT/envergo/pull/1391), et amélioration de l'accessibilité via l'affichage des références d'évaluation dans les titres de page.
- **Affichage des données** : Ajout de champs spécifiques pour l'affichage des Démarches Numériques (DN) pour les propriétaires [#1373](https://github.com/MTES-MCT/envergo/pull/1373) et pour les instructions [#1341](https://github.com/MTES-MCT/envergo/pull/1341).
- **Règles Métier** : Ajustement des contrôles pour le photovoltaïque (PV-Sol) et mise à jour des critères d'écoulement [#1366](https://github.com/MTES-MCT/envergo/pull/1366) ainsi que des évaluations EE30 [#1365](https://github.com/MTES-MCT/envergo/pull/1365).

### Évolutions techniques
- **Sécurité & Observabilité** : Création d'un tableau de bord de vulnérabilités avec scans nocturnés automatisés et intégration des données OSV [#1387](https://github.com/MTES-MCT/envergo/pull/1387). Correction de plusieurs failles de sécurité (fuite de clés secrètes, gestion des sessions et sécurisation de la déconnexion).
- **Montée de version majeure** : Migration vers Django 5.2 [#1336](https://github.com/MTES-MCT/envergo/pull/1336) et passage à PostgreSQL 17 (en CI et production).
- **Fiabilisation de la synchronisation** : Refonte complète de la méthode de synchronisation des Démarches Numériques (DN) pour la rendre transactionnelle, éviter les conflits de données et empêcher l'écrasement de dossiers existants [#1370](https://github.com/MTES-MCT/envergo/pull/1370).
- **Optimisation & Refactoring** : Extraction de méthodes pour améliorer la maintenabilité (gestion des logs, des notifications et des dates) et optimisation des processus de synchronisation pour éviter les exécutions concurrentes.

### Autres changements
- **Documentation** : Mise à jour de la documentation sur les démarches numériques [#967](https://github.com/MTES-MCT/envergo/pull/967) et du fichier README.
- **Nettoyage** : Suppression de commentaires obsolètes et nettoyage général du code.
