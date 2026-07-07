## Changelog : code-du-travail-numerique (30 derniers jours, au 03 juillet 2026)

### Résumé
Cette version apporte des améliorations à la recherche de conventions collectives, à l'affichage des accords d'entreprise et à la gestion des contributions. De plus, un système d'extraction et de vérification des événements de suivi a été mis en place pour assurer la qualité des données analytiques. Des corrections de bugs et des optimisations diverses ont également été implémentées.

### Évolutions fonctionnelles
- Ajout de la possibilité de rechercher des accords d'entreprise dans l'outil "Trouver sa convention collective" [#7260](https://github.com/SocialGouv/code-du-travail-numerique/issues/7260).
- Amélioration de l'affichage des accords d'entreprise, en les dissociant de la recherche d'entreprise [#7324](https://github.com/SocialGouv/code-du-travail-numerique/issues/7324).
- Ajout du type "bon à savoir" pour les contributions [#7326](https://github.com/SocialGouv/code-du-travail-numerique/issues/7326).
- Correction : Suppression de la condition d'ancienneté minimale pour les particuliers employeurs [#7314](https://github.com/SocialGouv/code-du-travail-numerique/issues/7314).
- Correction : Redirection de l'ancienne fiche canicule vers la nouvelle page d'information [#7318](https://github.com/SocialGouv/code-du-travail-numerique/issues/7318) et [#7322](https://github.com/SocialGouv/code-du-travail-numerique/issues/7322).
- Correction : Affichage correct des en-têtes de tableaux dans la section contribution [#7325](https://github.com/SocialGouv/code-du-travail-numerique/issues/7325).
- Correction : Normalisation de l'affichage du code IDCC 9999 [#7303](https://github.com/SocialGouv/code-du-travail-numerique/issues/7303).
- Correction : Blocage du bouton "Afficher les informations" sans convention collective sélectionnée [#7232](https://github.com/SocialGouv/code-du-travail-numerique/issues/7232).
- Correction : Ordre des accords par date de signature [#7313](https://github.com/SocialGouv/code-du-travail-numerique/issues/7313).

### Évolutions techniques
- Implémentation d'un système d'extraction et de vérification des événements de suivi (drift-check) [#7300](https://github.com/SocialGouv/code-du-travail-numerique/issues/7300).
- Génération de la documentation du plan de suivi (tracking plan) à partir des événements [#7343](https://github.com/SocialGouv/code-du-travail-numerique/issues/7343).
- Mise à jour de pnpm vers la version 11 et corrections associées [#7325](https://github.com/SocialGouv/code-du-travail-numerique/issues/7325).
- Ajout de logs pour le débogage de la recherche DILA.
- Améliorations et corrections mineures sur la POC accords d'entreprise [#7306](https://github.com/SocialGouv/code-du-travail-numerique/issues/7306).

### Autres changements
- Mise à jour des secrets pour l'environnement de pré-production.
- Suppression de la balise canonical sur la page générique de contribution [#7316](https://github.com/SocialGouv/code-du-travail-numerique/issues/7316).
- Publication des versions 4.231.0 à 4.232.0.
