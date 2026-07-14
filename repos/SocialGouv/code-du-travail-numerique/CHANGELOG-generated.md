## Changelog : code-du-travail-numerique (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette version apporte des améliorations à la recherche d'accords, à l'affichage des tableaux de contributions, et à la gestion des conventions collectives. De nouvelles fonctionnalités de suivi d'événements et de notation des contributions ont été ajoutées. Des corrections de bugs ont été apportées pour améliorer la stabilité et la précision des informations affichées.

### Évolutions fonctionnelles
- Ajout d'un widget de notation pour les contributions [#7344](https://github.com/SocialGouv/code-du-travail-numerique/issues/7344).
- Amélioration de la recherche d'accords en utilisant les accords de l'ES au lieu de l'API Legifrance [#7381](https://github.com/SocialGouv/code-du-travail-numerique/issues/7381).
- Correction de l'affichage des en-têtes de tableaux dans les contributions [#7325](https://github.com/SocialGouv/code-du-travail-numerique/issues/7325).
- Ajout du type "bon à savoir" pour les contributions [#7326](https://github.com/SocialGouv/code-du-travail-numerique/issues/7326).
- Correction de l'affichage des accords dans l'entreprise, en les dissociant de la recherche [#7324](https://github.com/SocialGouv/code-du-travail-numerique/issues/7324).
- Normalisation de l'affichage du code IDCC 9999 pour les conventions collectives [#7303](https://github.com/SocialGouv/code-du-travail-numerique/issues/7303).
- Redirection de l'ancienne fiche canicule vers la nouvelle page d'information [#7322](https://github.com/SocialGouv/code-du-travail-numerique/issues/7322) et [#7318](https://github.com/SocialGouv/code-du-travail-numerique/issues/7318).
- Correction pour ne plus exiger d'ancienneté minimale pour les particuliers employeurs [#7314](https://github.com/SocialGouv/code-du-travail-numerique/issues/7314).

### Évolutions techniques
- Mise en place d'un système d'extraction d'événements statiques et de vérification de la dérive [#7300](https://github.com/SocialGouv/code-du-travail-numerique/issues/7300).
- Génération de la documentation du plan de suivi (tracking plan) à partir des événements [#7343](https://github.com/SocialGouv/code-du-travail-numerique/issues/7343).
- Mise à jour de pnpm.
- Désactivation de Husky lors d'une release.

### Autres changements
- Ajout de logs pour la recherche DILA.
- Correction du canonical sur la page générique des contributions [#7316](https://github.com/SocialGouv/code-du-travail-numerique/issues/7316).
- Mise à jour des secrets pour la preprod.
- Correction de bugs suite au passage à pnpm 11.
- Amélioration de la fiabilité des tests E2E pour le glossaire, la recherche dans l'en-tête et les conventions collectives [#7319](https://github.com/SocialGouv/code-du-travail-numerique/issues/7319).
- Ordonnancement des accords par date de signature [#7313](https://github.com/SocialGouv/code-du-travail-numerique/issues/7313).
