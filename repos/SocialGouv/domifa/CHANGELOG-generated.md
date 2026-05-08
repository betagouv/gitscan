## Changelog : domifa (30 derniers jours, au 7 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment avec l'intégration de la bibliothèque DSFR et l'ajout d'une nouvelle page "Témoignages". Des corrections de bugs ont été implémentées pour améliorer la stabilité et la fiabilité de l'application, tant côté frontend que backend. Des optimisations ont également été apportées pour améliorer les performances et la sécurité.

### Évolutions fonctionnelles
- Ajout d'une page "Témoignages" pour afficher les témoignages utilisateurs. [#b31e412](https://github.com/SocialGouv/domifa/commit/b31e4126f75371db179d2ce1247d6d1180ebd1ec)
- Intégration de la bibliothèque DSFR (Design System for Government) pour améliorer l'accessibilité et l'apparence de l'interface utilisateur. [#f019654](https://github.com/SocialGouv/domifa/commit/f019654d14b8fe8141b12a35e94800f32c1675a9) et [#7e43c2a](https://github.com/SocialGouv/domifa/commit/7e43c2a10966424209a9042729289996f99a9114)
- Ajout de détails sur le réseau dans le backend. [#fb8f7d7](https://github.com/SocialGouv/domifa/commit/fb8f7d72740679fb87893b5242fc1451a0904470)
- Ajout d'un banner DSFR. [#b318698](https://github.com/SocialGouv/domifa/commit/b3186985639f19f0354621116b6941280415446f)

### Évolutions techniques
- Refactorisation du code pour récupérer les statistiques Metabase. [#81a0863](https://github.com/SocialGouv/domifa/commit/81a08639850479e7e0cdd37e6707f80961d7dd85)
- Ajout d'un mécanisme de limitation de débit (throttling) pour protéger le backend contre les requêtes excessives. [#e827fbc](https://github.com/SocialGouv/domifa/commit/e827fbc194459043886686254414966976434977)
- Amélioration de la sécurité en appliquant des règles de sécurité plus strictes. [#f82ddc5](https://github.com/SocialGouv/domifa/commit/f82ddc5a436986961f75868444a9378948246925)
- Ajout de logs pour faciliter le débogage et le suivi des performances. [#7ff4d66](https://github.com/SocialGouv/domifa/commit/7ff4d66d16f6096193994436944679396624b069)
- Mise à jour des DTO (Data Transfer Objects) pour renforcer la validation des données. [#d514d0d](https://github.com/SocialGouv/domifa/commit/d514d0d6494f27708b1616966949832a5691f97f) et [#bfd5e15](https://github.com/SocialGouv/domifa/commit/bfd5e1560295846698a6123407a3667759983004)
- Correction de problèmes liés aux tests unitaires. [#20fcd6b](https://github.com/SocialGouv/domifa/commit/20fcd6b5726926736a007f57f3186f749a390748)

### Autres changements
- Correction de divers bugs et améliorations de l'interface utilisateur.
- Suppression du bootstrap dans l'administration. [#dbc638c](https://github.com/SocialGouv/domifa/commit/dbc638ce8e297920049b875bc473f359496b8d9d)
- Correction de filtres backend. [#ccf2b29](https://github.com/SocialGouv/domifa/commit/ccf2b295e8a10ae738212d8a140db5758ea573b2)
- Ajout de la documentation CLAUSE.md [#1353b33](https://github.com/SocialGouv/domifa/commit/1353b336424646137310d4234f296f69809f1923)
