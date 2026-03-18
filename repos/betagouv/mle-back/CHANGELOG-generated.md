## Changelog : mle-back (30 derniers jours, au 10 mars 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'intégration de nouvelles sources de données de logements (Dossier Facile, Campus et Toits, CROUS, HSE Source, SAIEM Dragignan), l'amélioration de l'export des données, et l'ajout de statistiques et de suivi via Matomo. Des corrections de bugs et des améliorations de la robustesse du système ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la source de logements "Dossier Facile" avec gestion des webhooks et premiers cas d'utilisation.
- Intégration de la source "Campus et Toits".
- Importation des prix du CROUS via une commande dédiée.
- Ajout de la source "HSE Source".
- Ajout de la source "SAIEM Dragignan".
- Amélioration de l'export Excel : correction de l'affichage des disponibilités, ajout des prix minimum et maximum, intégration du CROUS.
- L'export Excel est désormais disponible via un lien de téléchargement.
- Ajout du champ "référence externe" pour faciliter la correspondance avec les API externes.
- Ajout des champs manquants aux sérialiseurs pour une meilleure gestion des données.
- Correction de l'affichage des slugs.

### Évolutions techniques
- Amélioration de la gestion du géocodage avec ajout de mécanismes de retry et gestion des noms de villes.
- Correction d'une faille de sécurité.
- Refonte partielle du service Matomo et ajout de variables d'environnement pour sa configuration.
- Ajout de statistiques et intégration de Matomo pour le suivi des événements.
- Mise à jour des dépendances : Ruff (0.14.14 -> 0.15.0) et Sentry SDK (2.51.0 -> 2.52.0).
- Ajout de tests pour les types de cible et de résidence.
- Correction de conflits de migrations.
- Ajout de la gestion des clés d'hôte pour sécuriser les connexions.
- Amélioration de la gestion des erreurs : journalisation des erreurs au lieu de les afficher à l'utilisateur.

### Autres changements
- Ajout de la gestion de la dernière connexion et de l'historisation des modifications utilisateur.
- Ajout de propriétaires (owners) et renommage de l'index généré par Claude.
- Ajout de variables d'environnement pour Matomo.
- Correction de tests et ajout de nouveaux tests pour améliorer la couverture.
- Ajout de commentaires pour désactiver temporairement la source "Fac Habitat" en production.
- Correction de l'encodage UTF-8 pour l'ouverture de fichiers.
- Ajout d'un nouveau fichier de verrouillage.
- Ajout de types pour améliorer la couverture des tests.
- Correction de la gestion des nombres à virgule flottante.
- Ajout de la gestion des URLs d'images non obligatoires.
