## Changelog : passemarche (30 derniers jours, au 10 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration du parcours de candidature, notamment en permettant aux utilisateurs de choisir explicitement leur mode de candidature (seul ou en groupement) et de définir le type juridique de leur groupement. L'expérience est fluidifiée par un nouveau système de navigation assistée (wizard) et l'ajout d'un mode de relecture pour valider les choix effectués.

### Évolutions fonctionnelles
- Choix du mode de candidature (seul ou en groupement) via un nouvel écran dédié [#484](https://github.com/datagouv/passemarche/pull/484).
- Ajout d'une étape pour définir le type juridique du groupement au cours du parcours [#489](https://github.com/datagouv/passemarche/pull/489).
- Mise en place d'un mode "lecture seule" permettant de revoir et valider le mode de candidature choisi [#489](https://github.com/datagouv/passemarche/pull/489).
- Amélioration de l'interface visuelle lors de la sélection du mode de candidature [#484](https://github.com/datagouv/passemarche/pull/484).
- Correction permettant de rendre l'adresse email optionnelle pour le mandataire d'un groupement [#484](https://github.com/datagouv/passemarche/pull/484).

### Évolutions techniques
- Refonte de la navigation du parcours (wizard) pour centraliser la logique de progression et améliorer la stabilité [#493](https://github.com/datagouv/passemarche/pull/493).
- Optimisation de l'architecture en extrayant les requêtes de lecture des contrôleurs vers des *presenters* dédiés.
- Amélioration de la structure du code en déplaçant la logique métier (`already_mandataire?`) du présentateur vers le modèle [#493](https://github.com/datagouv/passemarche/pull/493).
- Renforcement de la fiabilité des tests avec l'ajout de nouveaux scénarios Cucumber et la correction de l'ordre de certains tests de versioning.
- Correction de la propagation de l'utilisateur lors des connexions différées en mode mixte.

### Autres changements
- Ajout d'une tâche de maintenance (Rake task) pour permettre la conversion des anciennes candidatures vers le mode "solo".
