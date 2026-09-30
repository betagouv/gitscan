## Changelog : complements-alimentaires (30 derniers jours, au 29 septembre 2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'améliorations visant à fiabiliser la saisie des données (champs obligatoires, corrections de vocabulaire) et à améliorer le suivi des dossiers (nouvelle colonne de date, gestion des délais de visa). La stabilité technique et l'expérience utilisateur ont également été renforcées par l'optimisation des envois d'e-mails et la mise à jour des composants graphiques.

### Évolutions fonctionnelles
- Ajout d'une colonne "date de création" pour les dossiers de substances déclarées (SD) ([#3127](https://github.com/betagouv/complements-alimentaires/pull/3127)).
- Renforcement de la validation des formulaires : les champs "populations" et "effets" sont désormais obligatoires pour la soumission, avec un indicateur visuel pour l'utilisateur ([#3125](https://github.com/betagouv/complements-alimentaires/pull/3125)).
- Amélioration de la qualité des données Open Data via une correction du vocabulaire utilisé dans les exports.
- Optimisation de la gestion des visas : mise en place de valeurs par défaut automatiques, suivi des délais de traitement ([#3105](https://github.com/betagouv/complements-alimentaires/pull/3105)) et meilleure gestion des erreurs de navigation (404) sur les instructions de visa ([#3081](https://github.com/betagouv/complements-alimentaires/pull/3081)).
- Correction d'un dysfonctionnement lors de la procédure de vérification de l'adresse e-mail.

### Évolutions techniques
- Amélioration des performances et de la fiabilité de l'envoi d'e-mails grâce au passage en mode asynchrone pour le service Brevo ([#3074](https://github.com/betagouv/complements-alimentaires/pull/3074)).
- Mise à jour des composants graphiques du Design System (DSFR) pour les graphiques ([#3073](https://github.com/betagouv/complements-alimentaires/pull/3073)).
- Évolution de l'intégration avec ProConnect ([#3023](https://github.com/betagouv/complements-alimentaires/pull/3023)).
- Optimisation de la logique ETL pour la gestion des décisions de jeux de données ([#3115](https://github.com/betagouv/complements-alimentaires/pull/3115)).

### Autres changements
- Sécurité : ajout du fichier `security.txt`.
- Documentation : mise à jour de la documentation du projet.
- Maintenance : mise à jour de la configuration de l'outil de qualité de code ESLint.
