## Changelog : seves (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à Sèves au cours des 30 derniers jours. Les principales évolutions concernent l'amélioration de l'expérience utilisateur, notamment sur les pages de détail et de listes, ainsi que l'ajout de nouvelles fonctionnalités comme le téléchargement massif de documents et la gestion des verrous sur les TIAC et SSA. Des corrections de bugs et des optimisations de performance ont également été réalisées.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité de téléchargement massif de documents sur les fiches Seves (#1733).
- Amélioration des performances des pages de listes pour les TIAC et SSA.
- Amélioration de la vitesse de chargement des pages de détail pour tous les produits.
- Possibilité de restreindre les types de documents autorisés lors de l'édition d'un document.
- Ajout d'un mécanisme de verrouillage sur les TIAC et SSA pour éviter les conflits d'édition.
- Ajout de la possibilité de masquer des membres d'équipe dans les listes déroulantes.
- Amélioration de l'affichage des établissements (enseigne et raison sociale).
- Ajout de la possibilité de définir des liens libres via l'API.
- Ajout de nouvelles catégories de produits.
- Amélioration de l'historique des investigations TIAC.
- Ajout d'un indicateur pour les liens d'historique sur les SV.
- Possibilité de forcer une structure à être disponible en tant que contact.
- Ajout de nouvelles structures dans l'import Agricoll.
- Amélioration de l'affichage des valeurs de suivi pour les événements simples.
- Ajout d'une option de suivi pour les enregistrements simples.
- Amélioration de la recherche dans les listes ChoicesJs.
- Ajout d'un champ pour indiquer si un utilisateur doit être activé par défaut.

### Évolutions techniques
- Refactorisation du code pour préparer l'implémentation du téléchargement massif de documents asynchrone.
- Mise à jour de la configuration de Django pour permettre l'utilisation de partials dans les templates de formulaires.
- Utilisation de Ruff pour le tri des imports.
- Ajout du paramètre `--fix` au hook ruff de pre-commit.
- Amélioration des tests unitaires pour les documents.
- Optimisation des performances globales de l'application.
- Correction d'un bug de détection du type MIME pour les fichiers docx.
- Correction d'une vulnérabilité XSS dans la fonctionnalité de téléchargement massif de documents.
- Mise à jour de plusieurs dépendances : Ruff (0.15.0 -> 0.15.2), sqlparse (0.5.3 -> 0.5.4), virtualenv (20.29.1 -> 20.36.1), django-environ (0.12.0 -> 0.12.1), filelock (3.13.4 -> 3.20.3), pytest-django (4.11.1 -> 4.12.0), redis (7.1.0 -> 7.1.1), django-dirtyfields (1.9.8 -> 1.9.9), django-debug-toolbar (6.1.0 -> 6.2.0), urllib3 (2.5.0 -> 2.6.3), sentry-sdk[django] (2.49.0 -> 2.51.0), playwright (1.57.0 -> 1.58.0).

### Autres changements
- Modification du titre des pages de mise à jour des TIAC.
- Correction du filtre pour les agents et les structures pour les ICH.
- Correction d'un bug empêchant la filtration par date.
- Suppression d'une ancienne feature flag.
- Ajout d'une alerte/avertissement pour l'équipe en environnement de production.
- Amélioration des tests pour les listes SSA.
- Suppression de règles pour le champ RASFF sur les SSA.
- Ajout de Saint-Pierre-et-Miquelon dans la liste des départements.
- Amélioration de l'UX du composant LienLibre.
- Suppression d'éléments dupliqués dans la recherche en texte libre.
- Ajout de MUS au contact si MUS est concerné par le suivi.
- Séparation du champ "numero" en deux champs distincts.
- Limitation du nombre de caractères dans le nom de fichier pour les documents.
- Correction de plusieurs problèmes liés à l'inspection des dates.
- Ajout d'un préfixe pour les badges du nombre de participants pour les TIAC.
- Harmonisation des dates entre les TIAC et les SSA.
- Amélioration de la carte des établissements sur les SSA.
- Suppression du flag de page de révision sur les SSA/TIAC.
- Correction d'erreurs de messages vides lors du téléchargement massif.
- Ajout d'une variable d'environnement pour contrôler l'envoi des emails d'accès.
- Amélioration de l'affichage des lignes de précision sur la page d'édition.
- Correction de l'utilisation de l'URL par du texte dans les notifications par email.
- Ajout de DOM/TOM manquants.
- Amélioration de la gestion des erreurs lors du téléchargement massif de documents.
- Correction de l'affichage des messages d'erreur vides lors du téléchargement massif.
- Ajout de commentaires suite à la recette pour le téléchargement massif de documents.
