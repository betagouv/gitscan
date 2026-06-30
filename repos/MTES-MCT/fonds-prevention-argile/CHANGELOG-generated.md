## Changelog : fonds-prevention-argile (30 derniers jours, au 29 juin 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives pour les agents, notamment en termes d'accès aux dossiers, de gestion des demandes et de diagnostic des dossiers. Des corrections ont également été apportées pour améliorer la stabilité et la sécurité de l'application. Des fonctionnalités ont été ajoutées pour faciliter l'accès aux informations et la gestion des parcours utilisateurs.

### Évolutions fonctionnelles
- Les agents ont désormais la possibilité de distinguer un dossier à corriger d'un dossier renvoyé en construction dans l'espace agent. [#241](https://github.com/MTES-MCT/fonds-prevention-argile/issues/241)
- Les DDT ont désormais accès aux dossiers. [#230](https://github.com/MTES-MCT/fonds-prevention-argile/issues/230)
- Possibilité de ré-ouvrir une demande refusée par l'AMO. [#244](https://github.com/MTES-MCT/fonds-prevention-argile/issues/244)
- Les analystes peuvent désormais consulter le détail des demandes (lecture seule) pour les territoires. [#243](https://github.com/MTES-MCT/fonds-prevention-argile/issues/243)
- Ajout d'une vue diagnostic des dossiers DN pour faciliter l'analyse. [#228](https://github.com/MTES-MCT/fonds-prevention-argile/issues/228)
- Preremplissage de la démarche de diagnostic pour simplifier le processus. [#216](https://github.com/MTES-MCT/fonds-prevention-argile/issues/216)
- Ajout d'un bouton de copie des emails par onglet pour les agents. [#204](https://github.com/MTES-MCT/fonds-prevention-argile/issues/204)
- Ajout d'une route `/kit` redirigeant vers le kit de communication. [#206](https://github.com/MTES-MCT/fonds-prevention-argile/issues/206)
- Accès aux dossiers pour tous les agents. [#199](https://github.com/MTES-MCT/fonds-prevention-argile/issues/199)
- Persistance des filtres de dossiers dans l'URL pour une meilleure expérience utilisateur. [#205](https://github.com/MTES-MCT/fonds-prevention-argile/issues/205)
- Utilisation du nom de famille complet (et non seulement du nom de jeune fille) dans l'application. [#200](https://github.com/MTES-MCT/fonds-prevention-argile/issues/200)

### Évolutions techniques
- Correction des CVE openssl dans l'image de développement et réparation de la build Docker pour améliorer la sécurité. [#227](https://github.com/MTES-MCT/fonds-prevention-argile/issues/227)
- Mise en place d'un script pour réinitialiser les dossiers en validation AMO. [#219](https://github.com/MTES-MCT/fonds-prevention-argile/issues/219)
- Script de détachement AMO pour faciliter le passage en mode sans AMO. [#246](https://github.com/MTES-MCT/fonds-prevention-argile/issues/246)
- Correction d'erreurs de synchronisation DN. [#229](https://github.com/MTES-MCT/fonds-prevention-argile/issues/229)
- Correction du simulateur pour rendre non éligible un logement hors zone argileuse. [#215](https://github.com/MTES-MCT/fonds-prevention-argile/issues/215)
- Correction d'un bug empêchant la consultation du détail des dossiers sans AMO. [#223](https://github.com/MTES-MCT/fonds-prevention-argile/issues/223)
- Correction de l'affichage du menu d'actions coupé par la table dans l'espace agent. [#240](https://github.com/MTES-MCT/fonds-prevention-argile/issues/240)
- Correction des labels et de l'état des dossiers sans AMO. [#242](https://github.com/MTES-MCT/fonds-prevention-argile/issues/242)
- Correction d'un bug empêchant le relink d'une cible déjà rattachée à un autre parcours. [#238](https://github.com/MTES-MCT/fonds-prevention-argile/issues/238)
- Correction d'un problème d'ISR sur les pages RGA. [#239](https://github.com/MTES-MCT/fonds-prevention-argile/issues/239)
- Ajout d'une image de signature. [#248](https://github.com/MTES-MCT/fonds-prevention-argile/issues/248)

### Autres changements
- Mise à jour de la documentation des agents. [#202](https://github.com/MTES-MCT/fonds-prevention-argile/issues/202)
- Mise à jour de la clé d'encryption NEXT_SERVER_ACTIONS_ENCRYPTION_KEY dans le README. [#222](https://github.com/MTES-MCT/fonds-prevention-argile/issues/222)
- Mise à jour de la version à 1.14.0. [#220](https://github.com/MTES-MCT/fonds-prevention-argile/issues/220)
- Mise à jour des dépendances. [#224](https://github.com/MTES-MCT/fonds-prevention-argile/issues/224)
- Mise à jour de l'ADR Matomo. [#217](https://github.com/MTES-MCT/fonds-prevention-argile/issues/217)
