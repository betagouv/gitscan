## Changelog : nitrates (30 derniers jours, au 24 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives en matière de sécurité, notamment des correctifs pour des vulnérabilités identifiées lors d'un pentest. L'interface utilisateur a été améliorée, en particulier sur mobile, avec des ajustements pour l'accessibilité et l'expérience utilisateur. Des optimisations ont été apportées au processus de déploiement (GitOps) et à la gestion des données, ainsi que des corrections de bugs et des améliorations de la performance.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité du simulateur, notamment au niveau du clavier et du parcours utilisateur. [#215](https://github.com/betagouv/nitrates/issues/215)
- Affichage du contenu riche des pièces complémentaires même en cas de message d'erreur. [#216](https://github.com/betagouv/nitrates/issues/216)
- Amélioration du récapitulatif du calendrier avec des puces indentées et un ordre plus logique des périodes. [#159](https://github.com/betagouv/nitrates/issues/159)
- Adaptation de l'affichage du calendrier et du bandeau pour une meilleure expérience sur mobile. [#177](https://github.com/betagouv/nitrates/issues/177)
- Ajout d'une flèche de prévisualisation pour les catalogues de paramètres dans l'administration. [#218](https://github.com/betagouv/nitrates/issues/218) et [#219](https://github.com/betagouv/nitrates/issues/219)
- Possibilité de filtrer les données de validation par région Hauts-de-France.
- Amélioration du comparateur d'images dans la validation, avec affichage en galerie.
- Ajout d'un lien d'accès rapide vers la validation des feuilles dans l'interface d'administration.
- Affichage des points PAR (Présence Agricole Régionale) par région métropolitaine dans la prévisualisation.
- Simplification des libellés publics pour les vergers et les vignes.
- Amélioration de la gestion des renvois d'arbres et des contextes associés. [#222](https://github.com/betagouv/nitrates/issues/222)

### Évolutions techniques
- Mise en place d'un processus de déploiement GitOps avec des garde-fous pour les migrations, les arbres et les fixtures. [#50](https://github.com/betagouv/nitrates/issues/50)
- Correction de faux négatifs dans le smoke test CI. [#50](https://github.com/betagouv/nitrates/issues/50)
- Sécurisation de la page de connexion administrateur, désactivation du mot de passe par défaut et redirection vers ProConnect.
- Correction de plusieurs vulnérabilités de sécurité identifiées lors d'un pentest (reflected-XSS, etc.). [#150](https://github.com/betagouv/nitrates/issues/150)
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité (high/critical et medium).
- Amélioration de la couverture de test et exclusion des applications Envergo non-nitrates.
- Migration des données de référentiels vers une base de données native. [#226](https://github.com/betagouv/nitrates/issues/226)
- Refonte de la gestion des arbres et des snapshots. [#50](https://github.com/betagouv/nitrates/issues/50)
- Amélioration de la gestion des erreurs et des validations dans l'administration.

### Autres changements
- Mise à jour de la documentation et des textes de l'application. [#160](https://github.com/betagouv/nitrates/issues/160), [#177](https://github.com/betagouv/nitrates/issues/177)
- Correction de bugs mineurs et améliorations de la performance.
- Modification de l'intitulé de certaines questions et textes pour plus de clarté. [#192](https://github.com/betagouv/nitrates/issues/192)
- Ajout d'une illustration dédiée au thème sombre. [#190](https://github.com/betagouv/nitrates/issues/190)
- Amélioration du bandeau de construction pour une meilleure lisibilité. [#194](https://github.com/betagouv/nitrates/issues/194)
- Ajustements de l'interface utilisateur pour une meilleure expérience globale.
