## Changelog : fonds-prevention-argile (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives pour les agents, notamment dans la gestion des dossiers, l'accès aux informations et l'automatisation de certaines tâches. Des corrections de sécurité importantes ont également été apportées. De nouvelles fonctionnalités ont été ajoutées pour faciliter le diagnostic et le suivi des dossiers.

### Évolutions fonctionnelles
- Les agents peuvent désormais consulter le détail des dossiers même sans AMO. [#223](https://github.com/MTES-MCT/fonds-prevention-argile/issues/223)
- Ajout d'une vue diagnostic des dossiers DN pour les agents. [#228](https://github.com/MTES-MCT/fonds-prevention-argile/issues/228)
- Preremplissage automatique de la démarche diagnostic pour simplifier le processus. [#216](https://github.com/MTES-MCT/fonds-prevention-argile/issues/216)
- Les agents peuvent désormais copier facilement les adresses email par onglet. [#204](https://github.com/MTES-MCT/fonds-prevention-argile/issues/204)
- Ajout d'une route `/kit` redirigeant vers le kit de communication. [#206](https://github.com/MTES-MCT/fonds-prevention-argile/issues/206)
- Les agents peuvent maintenant accéder à tous les dossiers. [#199](https://github.com/MTES-MCT/fonds-prevention-argile/issues/199)
- Possibilité pour les agents d'ajouter des dossiers (AV / AMO / AV + AMO). [#195](https://github.com/MTES-MCT/fonds-prevention-argile/issues/195)
- Amélioration de l'affichage du nom de famille, en incluant le nom de jeune fille si nécessaire. [#200](https://github.com/MTES-MCT/fonds-prevention-argile/issues/200)
- Le simulateur ne considère plus comme éligible un logement situé hors zone argileuse. [#215](https://github.com/MTES-MCT/fonds-prevention-argile/issues/215)
- Les filtres de dossiers dans l'espace agent sont maintenant persistés dans l'URL. [#205](https://github.com/MTES-MCT/fonds-prevention-argile/issues/205)

### Évolutions techniques
- Correction des CVE openssl dans l'image de développement et réparation de la build Docker pour améliorer la sécurité. [#227](https://github.com/MTES-MCT/fonds-prevention-argile/issues/227)
- Mise à jour de la version de l'application à 1.14.0. [#220](https://github.com/MTES-MCT/fonds-prevention-argile/issues/220)
- Ajout d'un script d'opération pour réinitialiser un dossier en validation AMO. [#219](https://github.com/MTES-MCT/fonds-prevention-argile/issues/219)
- Correction de la logique d'URL dans le parcours pour éviter les erreurs. [#197](https://github.com/MTES-MCT/fonds-prevention-argile/issues/197)
- Correction d'un script orphelin lié au parcours. [#198](https://github.com/MTES-MCT/fonds-prevention-argile/issues/198)

### Autres changements
- Mise à jour de la documentation des agents. [#202](https://github.com/MTES-MCT/fonds-prevention-argile/issues/202)
- Mise à jour de la clé d'encryption NEXT_SERVER_ACTIONS_ENCRYPTION_KEY dans le README. [#222](https://github.com/MTES-MCT/fonds-prevention-argile/issues/222)
- Mise à jour des dépendances. [#224](https://github.com/MTES-MCT/fonds-prevention-argile/issues/224)
- Mise à jour de la configuration Matomo. [#217](https://github.com/MTES-MCT/fonds-prevention-argile/issues/217)
