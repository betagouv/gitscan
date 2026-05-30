## Changelog : code-du-travail-numerique (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, le projet a vu des améliorations significatives concernant le SMIC, avec l'ajout de méthodes de calcul et un support amélioré pour les contributions. La recherche a également été optimisée, et un quizz a été ajouté à la page d'accueil, bien qu'il soit actuellement désactivé. Plusieurs corrections de bugs ont été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- **SMIC :** Ajout de méthodes de calcul du SMIC annuel, permettant d'obtenir des informations plus précises. [#7286](https://github.com/SocialGouv/code-du-travail-numerique/issues/7286)
- **Contributions :** Support du "challenger" pour les modifications du SMIC lors de la soumission de contributions, facilitant la mise à jour des informations. [#7284](https://github.com/SocialGouv/code-du-travail-numerique/issues/7284)
- **Recherche :** Amélioration de la pertinence des résultats de recherche en ajustant le seuil de "fuzziness" pour la correspondance des définitions. [#7265](https://github.com/SocialGouv/code-du-travail-numerique/issues/7265) et [#7283](https://github.com/SocialGouv/code-du-travail-numerique/issues/7283)
- **Outils :** Ajout de la prise en compte de l'inaptitude non professionnelle dans le calcul du préavis de licenciement. [#7275](https://github.com/SocialGouv/code-du-travail-numerique/issues/7275)
- **Page d'accueil :** Ajout d'un quizz sur le code du travail (actuellement désactivé). [#7261](https://github.com/SocialGouv/code-du-travail-numerique/issues/7261)

### Évolutions techniques
- **Corrections de liens :** Mise à jour des liens vers Légifrance suite à leur passage au DSFR (format de données). [#7271](https://github.com/SocialGouv/code-du-travail-numerique/issues/7271)
- **Tests E2E :** Mise à jour des tests de bout en bout pour assurer la stabilité des fonctionnalités. [#7267](https://github.com/SocialGouv/code-du-travail-numerique/issues/7267)
- **Recherche :** Ajustement du "boost" sur les outils dans la recherche pour améliorer la pertinence des résultats. [#7266](https://github.com/SocialGouv/code-du-travail-numerique/issues/7266)

### Autres changements
- Correction d'un bug empêchant l'affichage correct de l'astérisque sur le brut des contributions. [#7288](https://github.com/SocialGouv/code-du-travail-numerique/issues/7288)
- Correction d'un problème d'ouverture incorrecte d'un accordéon dans la section des contributions. [#7278](https://github.com/SocialGouv/code-du-travail-numerique/issues/7278)
- Ajout d'attributs à la "whitelist" du challenger SMIC pour les contributions.
- Correction d'une valeur incorrecte du SMIC dans les contributions.
