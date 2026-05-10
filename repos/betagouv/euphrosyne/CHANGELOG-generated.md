## Changelog : euphrosyne (30 derniers jours, au 8 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'implémentation d'un nouveau système de gestion du cycle de vie des données des projets, permettant de gérer leur refroidissement (archivage) et leur disponibilité. Des améliorations ont également été apportées à l'interface utilisateur pour refléter ces changements et faciliter la gestion des projets. De plus, des mises à jour de dépendances et des corrections de bugs ont été intégrées pour améliorer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un support pour les watchers Goodflag, permettant de suivre l'état des fonctionnalités.
- Amélioration de l'interface utilisateur pour afficher l'état du cycle de vie des projets et bloquer les mutations sur les projets dans des états immuables.
- Implémentation d'un panneau d'administration pour gérer le cycle de vie des projets.
- Possibilité pour les leaders de modifier leur propre participation aux projets.
- Amélioration de l'interface utilisateur pour la liste des opérations de cycle de vie.
- Correction d'un bug empêchant l'utilisation de l'API d'initialisation des outils avec le slug du projet.
- Correction d'un bug dans le modal de planification pour éviter la soumission lors de la fermeture.
- Les administrateurs peuvent maintenant modifier les participations.
- Ajout d'une période de grâce avant de refroidir un projet.

### Évolutions techniques
- Implémentation d'un nouveau système de gestion du cycle de vie des données des projets (refroidissement, archivage).
- Refactorisation de l'API de gestion des données pour supporter le nouveau cycle de vie.
- Ajout d'une planification automatique quotidienne pour refroidir les projets éligibles.
- Mise en place d'un workflow de déploiement sur Scalingo lors de la publication de nouvelles versions.
- Mise à jour de nombreuses dépendances : Django (6.0.4), Pillow (12.2.0), axios (1.15.0), dotenv (17.4.0), mini-css-extract-plugin (2.10.2), vitest (4.1.5), typescript-eslint/eslint-plugin, jsdom, sentry/browser, webpack, cropperjs, prettier, etc.
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités.
- Amélioration de la gestion des erreurs et de la robustesse de l'application.
- Utilisation du slug du projet pour le renommage du répertoire du projet.
- Suppression du support Palissy pour POP.
- Utilisation de la nouvelle API POP et du service IIIF.

### Autres changements
- Ajout de documentation pour les nouvelles fonctionnalités de gestion du cycle de vie des données.
- Mise à jour des traductions françaises pour les nouveaux messages.
- Nettoyage du code et amélioration de la lisibilité.
- Ajout de variables d'environnement manquantes dans le fichier `.env.example`.
- Correction de la compatibilité de la vue Workplace lorsque la gestion des données est désactivée.
- Correction de l'appel de l'endpoint euphro tools avec le slug du projet.
- Ajout de commentaires et de documentation pour faciliter la maintenance du code.
- Suppression de l'importation de POP.
- Ajout de tests pour la récupération du cycle de vie.
- Ajout d'un endpoint pour obtenir l'ID d'opération.
- Ajout de la possibilité de restaurer des données.
- Amélioration de la gestion des erreurs lors de l'absence de `EUPHROSYNE_TOOLS_API_URL`.
- Ajout d'un plan initial pour la gestion du cycle de vie des données.
- Ajout d'un plan initial pour l'épique.
- Ajout de modèles RunData et LifecycleOperation.
- Amélioration de la logique d'éligibilité au refroidissement.
- Ajout de la possibilité de supprimer les données sources lors du refroidissement.
- Ajout de la possibilité de calculer la taille des données de run et le nombre de fichiers.
- Ajout de la commande `cool_project`.
- Ajout de la commande `data_management`.
- Ajout de la commande `restore`.
- Amélioration de la gestion des erreurs de démarrage de la gestion des données.
- Ajout de la possibilité de calculer la disponibilité des données du projet.
- Ajout d'un endpoint backend-to-backend pour le rôle de stockage du projet.
- Migration du bouton Virtual Office vers TypeScript.
- Amélioration des messages d'erreur et des traductions françaises.
- Correction de la compatibilité de la vue Workplace lorsque la gestion des données est désactivée.
- Correction de l'appel de l'endpoint de callback du cycle de vie pour exiger une authentification.
- Ajout de la possibilité de définir une date d'embargo pour le refroidissement.
- Augmentation de la durée par défaut du refroidissement à 24 mois.
- Ajout d'une gestion plus robuste des échecs de démarrage de la gestion des données.
- Ajout de la possibilité de définir un ID d'opération.
- Ajout de la possibilité de calculer la taille des données de run et le nombre de fichiers.
- Ajout de la commande `cool_project`.
- Ajout de la commande `data_management`.
- Ajout de la commande `restore`.
- Amélioration de la gestion des erreurs de démarrage de la gestion des données.
- Ajout de la possibilité de calculer la disponibilité des données du projet.
- Ajout d'un endpoint backend-to-backend pour le rôle de stockage du projet.
- Migration du bouton Virtual Office vers TypeScript.
- Amélioration des messages d'erreur et des traductions françaises.
- Correction de la compatibilité de la vue Workplace lorsque la gestion des données est désactivée.
- Correction de l'appel de l'endpoint de callback du cycle de vie pour exiger une authentification.
- Ajout de la possibilité de définir une date d'embargo pour le refroidissement.
- Augmentation de la durée par défaut du refroidissement à 24 mois.
- Ajout d'une gestion plus robuste des échecs de démarrage de la gestion des données.
- Ajout de la possibilité de définir un ID d'opération.
- Ajout de la possibilité de calculer la taille des données de run et le nombre de fichiers.
- Ajout de la commande `cool_project`.
- Ajout de la commande `data_management`.
- Ajout de la commande `restore`.
- Amélioration de la gestion des erreurs de démarrage de la gestion des données.
- Ajout de la possibilité de calculer la disponibilité des données du projet.
- Ajout d'un endpoint backend-to-backend pour le rôle de stockage du projet.
- Migration du bouton Virtual Office vers TypeScript.
- Amélioration des messages d'erreur et des traductions françaises.
- Correction de la compatibilité de la vue Workplace lorsque la gestion des données est désactivée.
- Correction de l'appel de l'endpoint de callback du cycle de vie pour exiger une authentification.
- Ajout de la possibilité de définir une date d'embargo pour le refroidissement.
- Augmentation de la durée par défaut du refroidissement à 24 mois.
- Ajout d'une gestion plus robuste des échecs de démarrage de la gestion des données.
- Ajout de la possibilité de définir un ID d'opération.
- Ajout de la possibilité de calculer la taille des données de run et le nombre de fichiers.
- Ajout de la commande `cool_project`.
- Ajout de la commande `data_management`.
- Ajout de la commande `restore`.
- Amélioration de la gestion des erreurs de démarrage de la gestion des données.
- Ajout de la possibilité de calculer la disponibilité des données du projet.
- Ajout d'un endpoint backend-to-backend pour le rôle de stockage du projet.
- Migration du bouton Virtual Office vers TypeScript.
- Amélioration des messages d'erreur et des traductions françaises.
