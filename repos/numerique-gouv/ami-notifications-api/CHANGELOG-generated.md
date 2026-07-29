## Changelog : ami-notifications-api (30 derniers jours, au 28 juillet 2026)

### Résumé
Cette période a été marquée par une refonte significative de l'interface utilisateur, notamment autour de la gestion des agendas et des suivis (anciennement "requests" et "inventory"). Des améliorations ont également été apportées à l'intégration avec FranceConnect et à l'API pour les événements, avec l'introduction d'une version 2. Des corrections de style et d'accessibilité ont été implémentées.

### Évolutions fonctionnelles
- **Services :** Ajout d'une nouvelle section "Services" dans le menu principal, permettant d'accéder à une liste de services disponibles via l'API.  Possibilité d'effectuer une authentification silencieuse (silent-login) pour ces services si activée. [#943](https://github.com/numerique-gouv/ami-notifications-api/issues/943)
- **Suivis (Followup) :** Renommage de la section "Requests" en "Suivis" pour plus de clarté.  Amélioration de l'affichage et de la navigation dans les suivis, avec une page de détail dédiée. [#266](https://github.com/numerique-gouv/ami-notifications-api/issues/266)
- **Agendas (Catalog) :** Renommage de la section "Inventory" en "Agendas" pour plus de cohérence.
- **Notifications :** Les notifications liées à un item redirigent désormais vers la page de suivi correspondante. [#1018](https://github.com/numerique-gouv/ami-notifications-api/issues/1018)
- **API Événements :** Introduction d'une version 2 de l'API pour les événements, avec l'ajout d'un champ "subheading" et des validations améliorées sur les champs parent. [#940](https://github.com/numerique-gouv/ami-notifications-api/issues/940)
- **Authentification FranceConnect :** Correction d'un problème de déconnexion intempestive de FranceConnect lors de l'authentification silencieuse. [#992](https://github.com/numerique-gouv/ami-notifications-api/issues/992)
- **Amélioration de l'expérience utilisateur :** Correction de problèmes de z-index et de styles pour améliorer l'affichage et l'accessibilité. [#950](https://github.com/numerique-gouv/ami-notifications-api/issues/950), [#1020](https://github.com/numerique-gouv/ami-notifications-api/issues/1020), [#1037](https://github.com/numerique-gouv/ami-notifications-api/issues/1037)

### Évolutions techniques
- **API :** Correction de la sérialisation du token OTVJWT. [#1070](https://github.com/numerique-gouv/ami-notifications-api/issues/1070)
- **Refactoring :** Refactorisation de la navigation principale et des composants d'en-tête pour améliorer la structure et les styles.
- **Mises à jour :** Mises à jour de plusieurs dépendances : Django (6.0.5 -> 6.0.6), ujson, msgpack, ws, undici, brace-expansion, soupsieve.

### Autres changements
- **Documentation :** Amélioration de la documentation et nettoyage du code.
- **Tests :** Ajout de tests pour les nouvelles fonctionnalités.
- **Configuration :** Ajout d'un feature flag pour activer/désactiver l'accès à la section "Services". [#943](https://github.com/numerique-gouv/ami-notifications-api/issues/943)
