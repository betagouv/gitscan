## Changelog : ami-notifications-api (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de la gestion d'éléments archivés pour les suivis, et l'implémentation d'une nouvelle méthode d'authentification via FranceConnect et une application dédiée (FI). Des améliorations techniques ont également été apportées pour optimiser la gestion des notifications et des abonnements push.

### Évolutions fonctionnelles
- **Suivis (Follow-up):** Ajout de la possibilité d'archiver des éléments de suivi. Cela inclut une page dédiée pour consulter les éléments archivés, une nouvelle fonctionnalité dans l'API pour gérer l'archivage, et une indication visuelle sur l'état archivé des éléments. [#776](https://github.com/numerique-gouv/ami-notifications-api/issues/776)
- **Authentification:** Implémentation d'une nouvelle méthode d'authentification via FranceConnect et une application dédiée (FI). Cela inclut la gestion des sessions, l'autorisation, l'obtention d'informations utilisateur et la déconnexion. [#917](https://github.com/numerique-gouv/ami-notifications-api/issues/917), [#907](https://github.com/numerique-gouv/ami-notifications-api/issues/907), [#708](https://github.com/numerique-gouv/ami-notifications-api/issues/708)
- **Gestion des adresses:** Amélioration de la gestion des adresses dans les préférences utilisateur, avec la possibilité de les ajouter, les supprimer et de les rechercher facilement. [#789](https://github.com/numerique-gouv/ami-notifications-api/issues/789)
- **Notifications:** Amélioration de l'affichage des liens dans les notifications pour rediriger vers la page de suivi correspondante. [#794](https://github.com/numerique-gouv/ami-notifications-api/issues/794)
- **Notifications:** Les notifications avec une date de validité dépassée ne sont plus incluses dans les listes. [#674](https://github.com/numerique-gouv/ami-notifications-api/issues/674)

### Évolutions techniques
- **Gestion des abonnements push:** Amélioration de la gestion des abonnements push lors de la réplication des enregistrements pour éviter les doublons. [#904](https://github.com/numerique-gouv/ami-notifications-api/issues/904)
- **Configuration:** Chargement de la variable d'environnement `DEBUG` à partir du fichier `.env.local` pour faciliter le débogage. [#905](https://github.com/numerique-gouv/ami-notifications-api/issues/905)
- **Authentification:** Paramétrisation des scopes utilisés pour l'authentification. [#907](https://github.com/numerique-gouv/ami-notifications-api/issues/907)
- **Base de données:** Optimisation des accès à la base de données pour la réplication des informations. [#904](https://github.com/numerique-gouv/ami-notifications-api/issues/904)
- **API:** Ajout du champ `content_private_body` aux modèles Notification et FollowUp, ainsi que dans les serializers correspondants. [#875](https://github.com/numerique-gouv/ami-notifications-api/issues/875)
- **Sécurité:** Correction d'une potentielle erreur d'intégrité lors de la déconnexion. [#971](https://github.com/numerique-gouv/ami-notifications-api/issues/971)

### Autres changements
- Mise à jour des dépendances : `uv`, `idna`, `ujson`, `vitest`, `@sveltejs/kit`, `ws`, `esbuild`, `@sveltejs/vite-plugin-svelte`, `vite`, `@vitejs/plugin-basic-ssl`, `webob`.
- Configuration de Vite pour LightningCSS.
- Nettoyage de fichiers inutiles.
- Amélioration de la gestion des cookies pour l'authentification FI.
- Suppression d'un dossier `.claude` résiduel.
- Correction de problèmes de scroll sur la page d'édition d'adresse.
- Amélioration de la gestion de la hauteur de la page sur Android WebView.
- Ajout de tests et de documentation.
