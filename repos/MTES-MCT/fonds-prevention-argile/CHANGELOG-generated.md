## Changelog : fonds-prevention-argile (30 derniers jours, au 10 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'espace agent, notamment la consultation des dossiers sans AMO, la persistance des filtres, et la copie des emails. De nouvelles fonctionnalités ont été ajoutées, comme l'accès à un kit de communication et la possibilité pour les agents de créer des dossiers (AV, AMO, AV+AMO). Des corrections ont également été apportées pour améliorer la stabilité et la logique de certaines fonctionnalités.

### Évolutions fonctionnelles
- Les agents peuvent désormais consulter le détail des dossiers sans AMO. [#223](https://github.com/MTES-MCT/fonds-prevention-argile/issues/223)
- Les filtres appliqués dans l'espace agent sont maintenant persistés dans l'URL, facilitant le partage et la navigation. [#205](https://github.com/MTES-MCT/fonds-prevention-argile/issues/205)
- Un bouton de copie des emails a été ajouté pour chaque onglet dans l'espace agent. [#204](https://github.com/MTES-MCT/fonds-prevention-argile/issues/204)
- Une nouvelle route `/kit` a été ajoutée pour accéder directement au kit de communication. [#206](https://github.com/MTES-MCT/fonds-prevention-argile/issues/206)
- Les agents peuvent maintenant créer des dossiers de type AV, AMO ou AV+AMO. [#195](https://github.com/MTES-MCT/fonds-prevention-argile/issues/195)
- Amélioration de l'affichage du nom de famille, en utilisant le nom de famille complet et non uniquement le nom de jeune fille. [#200](https://github.com/MTES-MCT/fonds-prevention-argile/issues/200)
- Ajout d'un champ "autre raison" manquant lors de la création de dossiers. [#196](https://github.com/MTES-MCT/fonds-prevention-argile/issues/196)
- Les agents ont maintenant accès à la liste de tous les dossiers. [#199](https://github.com/MTES-MCT/fonds-prevention-argile/issues/199)

### Évolutions techniques
- Script d'opération ajouté pour réinitialiser les dossiers en validation AMO. [#219](https://github.com/MTES-MCT/fonds-prevention-argile/issues/219)
- Correction de la logique de l'URL dans l'état "parcours". [#197](https://github.com/MTES-MCT/fonds-prevention-argile/issues/197)
- Correction d'un script orphelin lié aux parcours. [#198](https://github.com/MTES-MCT/fonds-prevention-argile/issues/198)
- Mise à jour de la clé d'encryption `NEXT_SERVER_ACTIONS_ENCRYPTION_KEY` dans le fichier README. [#222](https://github.com/MTES-MCT/fonds-prevention-argile/issues/222)
- Mise à jour de la configuration Matomo (ADR). [#217](https://github.com/MTES-MCT/fonds-prevention-argile/issues/217)
- Bump de la version à 1.14.0. [#220](https://github.com/MTES-MCT/fonds-prevention-argile/issues/220)

### Autres changements
- Mise à jour de la documentation pour les agents. [#202](https://github.com/MTES-MCT/fonds-prevention-argile/issues/202)
- Ajout d'actions. [#203](https://github.com/MTES-MCT/fonds-prevention-argile/issues/203)
