## Changelog : domifa (30 derniers jours, au 12 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives en matière de sécurité avec l'ajout d'un système de blocage de bots et la gestion des comptes bloqués. Des fonctionnalités d'administration ont été ajoutées, notamment la liste des utilisateurs. L'interface utilisateur a également été améliorée avec l'ajout d'informations et de corrections de bugs, ainsi que l'intégration de la nouvelle charte graphique DSFR.

### Évolutions fonctionnelles
- Ajout d'une page "Témoignages" en frontend. [#b31e412](https://github.com/SocialGouv/domifa/commit/b31e41297371b141798f26619988699d5764a157)
- Ajout d'un indicateur d'information (news) en frontend. [#39dc89a](https://github.com/SocialGouv/domifa/commit/39dc89a4a8522c410957d1a25d58b9f864fcd77d)
- Ajout d'une liste des utilisateurs dans l'interface d'administration. [#e74e9e9](https://github.com/SocialGouv/domifa/commit/e74e9e99960ad908d1760b16e1de04f47d195b0a)
- Possibilité de bloquer et débloquer des comptes utilisateurs en backend. [#3dfc13a](https://github.com/SocialGouv/domifa/commit/3dfc13adb9906ebc28efd9856b80d319286802aa) et [#08d3851](https://github.com/SocialGouv/domifa/commit/08d385161e5470fcb8021a97b447a666b40644cb)
- Ajout d'un statut pour les comptes bloqués en backend. [#c6a336b](https://github.com/SocialGouv/domifa/commit/c6a336b0619a182360f78a9a98d45588501b73d6)
- Intégration de la charte graphique DSFR (Design System FR) en frontend, incluant la suppression du changelog et l'ajout de la bannière DSFR. [#7e43c2a](https://github.com/SocialGouv/domifa/commit/7e43c2a9753309b569f9496545f15475f6a6f21d) et [#b318698](https://github.com/SocialGouv/domifa/commit/b3186981634463949979377826c6980684561356)
- Amélioration de l'affichage des statistiques Metabase. [#81a0863](https://github.com/SocialGouv/domifa/commit/81a08639850479e7e0cdd37e6707f80961d7dd85)

### Évolutions techniques
- Ajout d'un système de limitation de requêtes (throttling) pour prévenir les abus. [#e827fbc](https://github.com/SocialGouv/domifa/commit/e827fbc4988b96093f6666176b391254f270662e)
- Refactorisation des DTO (Data Transfer Objects) pour améliorer la validation et la sécurité des données. [#bfd5e15](https://github.com/SocialGouv/domifa/commit/bfd5e156a599a649498f905b133f194319447b0a) et [#f76159a](https://github.com/SocialGouv/domifa/commit/f76159a32185430469f9426462f559795999b97f)
- Amélioration des tests unitaires pour une meilleure couverture du code.
- Mise à jour des dépendances et correction de problèmes liés aux mises à jour de packages. [#a4a6ac2](https://github.com/SocialGouv/domifa/commit/a4a6ac2242d23148f612123e9312d1071735c13f)

### Autres changements
- Correction de bugs mineurs dans l'interface utilisateur, notamment concernant l'impression et l'affichage des listes. [#cd3a592](https://github.com/SocialGouv/domifa/commit/cd3a5929920216f629505976f496656b2f967643) et [#827255d](https://github.com/SocialGouv/domifa/commit/827255d85594f5f2b05178b81760707637c66351)
- Correction de problèmes liés à la configuration des filtres. [#ccf2b29](https://github.com/SocialGouv/domifa/commit/ccf2b295e8a10ae738212d8a140db5758ea573b2)
- Suppression de Bootstrap dans l'interface d'administration. [#dbc638c](https://github.com/SocialGouv/domifa/commit/dbc638ce8e297920049b875bc473f359496b8d9d)
- Correction de problèmes liés aux champs de formulaire et à la page RGAa. [#d3300cb](https://github.com/SocialGouv/domifa/commit/d3300cb539f477949a324599469642148f94771a)
- Ajout d'un fichier CLAude.md. [#1353b33](https://github.com/SocialGouv/domifa/commit/1353b3354033429059265f7786f6676294f64b2a)
