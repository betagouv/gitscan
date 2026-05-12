## Changelog : cdata (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, l'application cdata a bénéficié d'une refonte significative avec la migration vers Nuxt 4.4, apportant des améliorations de performance et de nouvelles fonctionnalités. L'expérience utilisateur a été enrichie avec l'ajout d'une nouvelle page d'exploration tabulaire des données, des améliorations de la recherche et de la visualisation, ainsi que des optimisations pour les pages d'organisation.

### Évolutions fonctionnelles
- **Recherche :**
    - Ajout de filtres personnalisés et d'une meilleure gestion des types pour une recherche plus précise [#1067].
    - Possibilité de configurer le placeholder de la barre de recherche [#1059].
    - Correction d'un bug empêchant la suppression des filtres personnalisés [#1064].
- **Exploration des données :**
    - Nouvelle page d'exploration tabulaire des données, offrant une nouvelle façon d'interagir avec les jeux de données [#971, #1072].
    - Amélioration de la réactivité de l'explorateur de ressources [#1014].
- **Pages d'organisation :** Nouvelle mise en page pour les pages d'organisation, améliorant la présentation et l'ergonomie [#1051].
- **Documentation :** Ajout de documentation sur l'obtention d'une clé API pour la démo [#1045].
- **Activité :** Affichage de l'activité pour les membres d'une organisation [#1052].
- **Callbacks :** Affichage des callbacks en attente et ajout du sujet utilisateur [#1073].
- **Guides :** Correction des URLs des guides [#1077] et ajout d'un lien vers le score de qualité [#1061].
- **Swagger :** Affichage de la documentation Swagger pour l'API [#1055].
- **SEO :** Améliorations du référencement naturel (SEO) [#1066].

### Évolutions techniques
- **Migration Nuxt :** Mise à jour vers Nuxt 4.4, incluant les versions intermédiaires 4.1, 4.2, et 4.3 [#1035, #1037, #1038, #1047].
- **Optimisations :** Utilisation d'images SVG optimisées avec svgo [#1057].
- **Correction Nitro :** Correction d'un patch pour le serveur Nitro de Nuxt [#1053].
- **Gestion des dépendances :** Mise à jour des dépendances du projet [#1060].
- **Configuration :** Alignement du README avec Nuxt 4 [#1068].
- **Ignorer pnpm store :** Ajout d'une règle pour ignorer le répertoire local du cache pnpm [#1071].

### Autres changements
- Correction d'un bug lié à l'initialisation des fonctionnalités du collecteur sur le premier chargement de page [#1043].
- Correction de problèmes de débordement de cellules dans le tableau de bord de modération [#1050].
- Amélioration de l'affichage des blocs dans les articles [#1027].
- Correction de redirections cassées dans la configuration [#1065].
- Correction d'un problème de signature `mobileVisibleFields` [#1058].
- Ajout de configurations multiples pour la même classe dans la recherche [#1049].
- Correction d'un bug lié à l'affichage des SVG statiques [#1056].
- Ajout de tabs pour filtrer les types de sujets dans le tableau de bord de modération [#1033].
- Amélioration de l'affichage des suggestions d'IA dans les formulaires [#1046].
