## Changelog : seves (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions de Sèves se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans les modules de Surveillance Végétale (SV) et de Surveillance Sanitaire Animale (SSA). Des améliorations ont été apportées à la gestion des données, à l'affichage des informations, et à l'ajout de nouvelles fonctionnalités comme la cartographie et la gestion des éléments infestés. Des corrections de bugs et des optimisations de performance ont également été réalisées.

### Évolutions fonctionnelles
- Ajout de la possibilité d'afficher une carte lors de la création et de la consultation d'un lieu en SV.
- Intégration d'un panneau "éléments infestés" dans le formulaire SV.
- Amélioration de la recherche d'espèces dans SV, désormais gérée par un contrôleur Stimulus dédié.
- Ajout de la possibilité de télécharger des documents au format DOCX, même sans date de publication.
- Amélioration de l'affichage des sauts de ligne dans les messages.
- Ajout de la possibilité de télécharger des documents dans une archive ZIP.
- Amélioration de l'historique des modifications en SV.
- Ajout d'un indicateur pour les fiches de zone délimitée dans le tableau des événements SV, avec amélioration de l'accessibilité.
- Mise en place d'un nouveau widget Treeselect dans SSA, améliorant l'expérience utilisateur pour la sélection d'éléments.
- Ajout de l'ON (Organisme Notifié) pour SV.
- Amélioration des messages d'information dans SSA.
- Ajout d'une page d'accessibilité.
- Possibilité de prévisualiser les images et les fichiers PDF.
- Correction de l'affichage des filtres d'année et de numéro.

### Évolutions techniques
- Migration du modèle SiteInspection vers un type de choix texte.
- Refactorisation du code pour améliorer la réutilisabilité de la page ChoiceJSPage.
- Amélioration de la gestion des erreurs OIDC pour éviter les interruptions de processus en production.
- Mise à jour de plusieurs dépendances : Django, Gunicorn, urllib3, Playwright, Sentry, psycopg2-binary, pre-commit, lxml, django-dsfr, django-post-office, pytest, ruff.
- Suppression de l'utilisation de SSA dans l'application core.
- Amélioration de la connexion Celery à Redis.
- Correction de conflits de migration.
- Ajout de tests et corrections pour la cartographie en SV.
- Uniformisation des liens d'annulation sur les fiches d'objets.
- Amélioration des performances de la vue de liste SSA.

### Autres changements
- Suppression du flag de fonctionnalité pour l'éditeur de texte enrichi.
- Suppression du flag de fonctionnalité pour le téléchargement ZIP.
- Correction de problèmes de compatibilité avec le navigateur Brave.
- Correction de problèmes liés à l'ellipsis tooltip dans TIAC.
- Désactivation des avertissements Python dans le CI pour améliorer la lisibilité.
- Amélioration de la configuration du reporter de tests dorny/test-reporter@v1.
- Correction de bugs mineurs liés à l'éditeur de texte enrichi.
- Ajout de noms relatifs dans SV pour la zone infestée.
- Correction de problèmes liés à la date de publication dans l'export DOCX.
- Correction de bugs liés à l'affichage des données dans les tests.
- Ajout de contraintes pour les sources vides.
