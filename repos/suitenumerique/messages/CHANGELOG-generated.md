## Changelog : messages (30 derniers jours, au 28 septembre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec une refonte complète de l'interface utilisateur de l'application mobile pour une expérience plus fluide. Les administrateurs de domaine disposent désormais de nouvelles capacités d'exportation de boîtes de réception, tandis que l'expérience sur le web a été enrichie par la possibilité de rédiger des messages dans des fenêtres flottantes et une meilleure mémorisation des préférences de navigation.

### Évolutions fonctionnelles
- **Expérience Mobile** : Refonte complète de l'interface utilisateur (UI overhaul) et amélioration de l'ergonomie (gestion du clavier, focus du rédacteur et support du mode paysage).
- **Expérience Web** : Introduction de la rédaction de messages dans des fenêtres flottantes.
- **Navigation** : Amélioration de la fluidité avec la mémorisation de la dernière boîte de réception active et redirection automatique vers l'inbox lors d'un changement de boîte.
- **Administration** : Possibilité pour les administrateurs de domaine d'exporter des boîtes de réception [#789](https://github.com/suitenumerique/messages/issues/789).
- **Gestion des messages** : Amélioration du support du format mbox (gestion des mots-clés) et exclusion par défaut des spams et de la corbeille des statistiques.
- **Corrections** : Résolution de problèmes sur le popover de recherche (tablettes), le parsing des noms de dossiers IMAP et l'affichage des expéditeurs dans les fils de discussion.
- **API** : Ajout de la gestion des canaux lors de l'utilisation de l'API de soumission [#794](https://github.com/suitenumerique/messages/issues/794).

### Évolutions techniques
- **Infrastructure Mobile** : Mise à jour de Capacitor (v8.5), adoption du cycle de vie UIScene et automatisation de la publication des mises à jour "Over-The-Air" (OTA) depuis Scalingo.
- **Sécurité** : 
    - Renforcement de la protection via l'ajout de listes d'autorisation d'IP (allowlists) pour la console Keycloak [#793](https://github.com/suitenumerique/messages/issues/793) et l'administration Django.
    - Gestion de la suspension des clés API personnelles et des brouillons [#804](https://github.com/suitenumerique/messages/issues/804).
    - Durcissement des workflows GitHub Actions.
- **Backend** : Optimisation des performances en déplaçant les tâches d'exportation vers le worker d'importation [#805](https://github.com/suitenumerique/messages/issues/805).
- **Frontend** : Migration vers les nouveaux packages `ui-kit` et optimisation du redimensionnement des iframes de mails via `ResizeObserver`.
- **Maintenance** : Mise à jour de Keycloak [#798](https://github.com/suitenumerique/messages/issues/798) et amélioration du fuzzing pour `jmap-email` [#792](https://github.com/suitenumerique/messages/issues/792).

### Autres changements
- **Documentation** : Restructuration de la documentation mobile en guides distincts (onboarding et release).
- **Design** : Régénération des icônes et des écrans de démarrage (splash screens) de l'application mobile.
- **Versioning** : Mise à jour de la distribution et des packages [#800](https://github.com/suitenumerique/messages/issues/800).
