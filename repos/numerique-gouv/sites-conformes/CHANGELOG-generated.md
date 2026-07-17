## Changelog : sites-conformes (30 derniers jours, au 16 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations concernant la gestion des notifications, avec l'ajout d'un panneau d'information et la refactorisation du code existant. Des tests automatisés (E2E) ont également été implémentés pour améliorer la qualité et la stabilité du site. Des corrections de traductions et des ajustements mineurs ont été apportés pour améliorer l'expérience utilisateur et la maintenabilité du code.

### Évolutions fonctionnelles
- Ajout d'un panneau d'information pour afficher des notifications aux utilisateurs. Ce panneau inclut une date de début, une date de fin et un lien vers plus d'informations. [#555](https://github.com/numerique-gouv/sites-conformes/issues/555)
- Amélioration de la gestion des traductions, notamment pour les blocs d'images imbriqués, corrigeant ainsi une erreur 500 lors de la traduction de pages.
- Ajout de la possibilité de choisir la balise de titre (heading) dans les blocs "stepper".
- Ajout de tags avec un titre.
- Amélioration de l'affichage des dates dans les entrées du bloc "événements récents".

### Évolutions techniques
- Implémentation de tests E2E (End-to-End) avec Playwright, incluant des tests visuels et une intégration continue (CI) pour détecter les régressions.
- Refactorisation du code des notifications, améliorant la logique, ajoutant de la journalisation et configurant les forks.
- Mise à jour de la version de tarteaucitronjs.
- Utilisation de `manage.py` pour les commandes `makemessages` et `compilemessages` pour une meilleure cohérence.
- Amélioration du script de restauration des médias locaux pour une meilleure gestion des erreurs et une sortie plus concise.
- Dérivation de la version du projet à partir des métadonnées du package pour garantir une source unique de vérité.
- Utilisation du composant de notification DSFR au lieu du CSS personnalisé.

### Autres changements
- Ajout de traductions manquantes.
- Mise à jour de la documentation pour proconnect après la packagification.
- Nettoyage du code et suppression de commentaires inutiles.
- Correction de divers problèmes mineurs liés aux migrations et aux traductions.
- Ajout de commentaires et de documentation pour faciliter la maintenance du code.
- Amélioration de la gestion des migrations.
- Suppression de listes ordonnées inutiles dans les champs de flux.
- Correction de l'alignement des divs dans les champs rich text.
