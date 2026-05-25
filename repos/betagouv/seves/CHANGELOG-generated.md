## Changelog : seves (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les évolutions de Sèves se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des enquêtes sanitaires (SV) avec l'ajout de cartes, la gestion des éléments infestés, et des corrections pour l'export de documents. Des améliorations techniques ont également été apportées pour la fiabilité des tests et la gestion des dépendances.

### Évolutions fonctionnelles
- Ajout de la possibilité d'afficher une carte lors de la création d'un lieu dans une enquête sanitaire (SV). [#912e1c0](https://github.com/betagouv/seves/commit/912e1c0)
- Ajout d'un panneau pour la gestion des éléments infestés dans le formulaire SV. [#8772c4e](https://github.com/betagouv/seves/commit/8772c4e)
- Amélioration de l'affichage des informations sur les lieux et les prélèvements dans la page de détails d'une enquête SV. [#a4f8599](https://github.com/betagouv/seves/commit/a4f8599)
- Ajout de la possibilité de télécharger les documents associés à une enquête dans une archive ZIP. [#9a688f1](https://github.com/betagouv/seves/commit/9a688f1)
- Amélioration de l'affichage des sauts de ligne dans les messages. [#bec903b](https://github.com/betagouv/seves/commit/bec903b)
- Ajout d'une page d'accessibilité. [#50fa32f](https://github.com/betagouv/seves/commit/50fa32f)
- Implémentation d'un nouveau sélecteur d'arbre (Treeselect) dans l'interface SSA. [#912e1c0](https://github.com/betagouv/seves/commit/912e1c0) et [#fce56df](https://github.com/betagouv/seves/commit/fce56df)
- Ajout de l'ON (Organisme Notifié) pour les enquêtes SV. [#6b49448](https://github.com/betagouv/seves/commit/6b49448)
- Ajout de l'ON Phytophthora kernoviae. [#f0dc0ec](https://github.com/betagouv/seves/commit/f0dc0ec)

### Évolutions techniques
- Suppression du *feature flag* pour l'éditeur de texte enrichi, le rendant désormais actif par défaut. [#f8fe6ed](https://github.com/betagouv/seves/commit/f8fe6ed)
- Suppression du *feature flag* pour le téléchargement en ZIP. [#b9881ab](https://github.com/betagouv/seves/commit/b9881ab)
- Refactorisation de l'approche de mise à jour des enquêtes SV. [#c827b59](https://github.com/betagouv/seves/commit/c827b59)
- Amélioration de la fiabilité des tests, notamment sur la page d'administration et pour les cartes SV. [#4c125fb](https://github.com/betagouv/seves/commit/4c125fb) et [#8857987](https://github.com/betagouv/seves/commit/8857987)
- Migration du modèle SiteInspection vers un TextChoices. [#8386f51](https://github.com/betagouv/seves/commit/8386f51)
- Modification de l'API ChoiceJSPage pour la rendre réutilisable. [#35de83e](https://github.com/betagouv/seves/commit/35de83e)

### Autres changements
- Correction d'un conflit de migration entre deux migrations. [#ba0fb8a](https://github.com/betagouv/seves/commit/ba0fb8a)
- Correction de problèmes d'affichage des PDF dans le navigateur Brave. [#5565d54](https://github.com/betagouv/seves/commit/5565d54)
- Correction d'un problème de CSP (Content Security Policy) pour Brave/Chromium. [#b95c150](https://github.com/betagouv/seves/commit/b95c150)
- Amélioration du format d'export CSV pour les enquêtes TIAC. [#9185ac3](https://github.com/betagouv/seves/commit/9185ac3)
- Amélioration de l'historique des enquêtes SV. [#2055cfe](https://github.com/betagouv/seves/commit/2055cfe) et [#042c1db](https://github.com/betagouv/seves/commit/042c1db)
- Diverses corrections et améliorations de l'interface utilisateur et des tests.
- Mise à jour de plusieurs dépendances (Sentry, Playwright, Django, etc.). Ces mises à jour sont de routine et n'impactent pas directement l'utilisateur final.
