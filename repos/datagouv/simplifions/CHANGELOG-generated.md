## Changelog : simplifions (30 derniers jours, au 09 septembre 2026)

### Résumé
Ce mois a marqué une étape majeure avec la mise en service de la nouvelle version du catalogue. L'interface est désormais pleinement opérationnelle, offrant une expérience de recherche et de navigation fluide, tout en assurant une continuité visuelle et technique avec l'ancien site. Les fonctionnalités de recherche, de filtrage et les pages de détails (solutions, cas d'usage, démarches) sont désormais disponibles et optimisées.

### Évolutions fonctionnelles
- **Recherche et navigation :** Mise en place d'un système complet de recherche, de filtrage par facettes et de tri au sein du catalogue [#22](https://github.com/datagouv/simplifions/pull/22). La page d'accueil est désormais connectée aux listes du catalogue.
- **Pages de détails :** Déploiement des pages dédiées pour les "Solutions" [#21](https://github.com/datagouv/simplifions/pull/21), les "Cas d'usage" [#17](https://github.com/datagouv/simplifions/pull/17) et les "Démarches" [#10](https://github.com/datagouv/simplifions/pull/10), avec un rendu fidèle à l'ancienne interface.
- **Optimisation SEO :** Amélioration du référencement naturel via l'implémentation des balises meta (titres, descriptions, Open Graph), du sitemap.xml et du robots.txt [#27](https://github.com/datagouv/simplifions/issues/27).
- **Expérience utilisateur (UX) :** 
    - Suppression du bandeau "version en construction" et du lien de connexion [#30](https://github.com/datagouv/simplifions/issues/30).
    - Amélioration de la visibilité des moyens d'accès et des liens directs vers la donnée sur les fiches démarches [#31](https://github.com/datagouv/simplifions/issues/31).
    - Affichage de messages explicites lorsque les filtres de recherche ne retournent aucun résultat.
    - Généralisation de l'affichage des dates en français sur l'ensemble du site.
- **Présentation des données :** Les recommandations des démarches sont désormais présentées selon l'ordre défini dans la feuille de calcul Grist [#33](https://github.com/datagouv/simplifions/issues/33).

### Évolutions techniques
- **Architecture et URLs :** Migration vers un modèle où le catalogue est l'unique source de vérité pour les listes et les fiches. Les anciens slugs (URLs) sont préservés pour garantir la continuité des liens existants [#29](https://github.com/datagouv/simplifions/issues/29).
- **Gestion des données :** 
    - Refonte du modèle d'importation pour permettre des imports "rejouables" depuis Grist [#8](https://github.com/datagouv/simplifions/pull/8).
    - Amélioration de la gestion des fichiers via Active Storage.
    - Mise en place de règles de validation plus strictes lors de l'import (refus des solutions privées ou des contenus incomplets).
- **Performances et rendu :** 
    - Implémentation du filtrage et du tri des intégrateurs côté client.
    - Sécurisation du rendu du contenu Markdown dans les vues.

### Autres changements
- Nettoyage de la base de données (suppression de colonnes inutilisées).
- Harmonisation du design pour un rendu "pixel-perfect" avec l'ancienne version.
