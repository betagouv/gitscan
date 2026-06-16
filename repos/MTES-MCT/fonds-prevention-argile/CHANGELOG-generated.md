## Changelog : fonds-prevention-argile (30 derniers jours, au 10 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'espace agent, notamment la consultation des détails des dossiers sans AMO, la persistance des filtres de dossiers et la possibilité de copier les adresses email des agents. De nouvelles fonctionnalités ont également été ajoutées, comme l'accès à un kit de communication et la création de dossiers par les agents.

### Évolutions fonctionnelles
- Les agents peuvent désormais consulter le détail des dossiers sans AMO. [#223](https://github.com/MTES-MCT/fonds-prevention-argile/issues/223)
- Les filtres appliqués à la liste des dossiers dans l'espace agent sont maintenant conservés dans l'URL, permettant de les partager et de les retrouver facilement. [#205](https://github.com/MTES-MCT/fonds-prevention-argile/issues/205)
- Un bouton de copie des adresses email a été ajouté dans l'onglet des agents, facilitant la communication. [#204](https://github.com/MTES-MCT/fonds-prevention-argile/issues/204)
- Une nouvelle route `/kit` a été ajoutée pour accéder directement au kit de communication. [#206](https://github.com/MTES-MCT/fonds-prevention-argile/issues/206)
- Les agents peuvent maintenant créer des dossiers de type AV, AMO ou AV + AMO. [#195](https://github.com/MTES-MCT/fonds-prevention-argile/issues/195)
- Les agents ont désormais accès à la liste de tous les dossiers. [#199](https://github.com/MTES-MCT/fonds-prevention-argile/issues/199)
- Amélioration de l'affichage du nom des utilisateurs, utilisant le nom de famille et non uniquement le nom de jeune fille. [#200](https://github.com/MTES-MCT/fonds-prevention-argile/issues/200)

### Évolutions techniques
- Ajout d'un script pour réinitialiser les dossiers en validation AMO. [#219](https://github.com/MTES-MCT/fonds-prevention-argile/issues/219)
- Mise à jour de la documentation de l'agent. [#202](https://github.com/MTES-MCT/fonds-prevention-argile/issues/202)
- Mise à jour de la configuration Matomo. [#217](https://github.com/MTES-MCT/fonds-prevention-argile/issues/217)
- Correction de la logique d'URL dans l'état du parcours. [#197](https://github.com/MTES-MCT/fonds-prevention-argile/issues/197)
- Correction d'un script orphelin et du code associé. [#198](https://github.com/MTES-MCT/fonds-prevention-argile/issues/198)

### Autres changements
- La version de l'application a été mise à jour à 1.14.0. [#220](https://github.com/MTES-MCT/fonds-prevention-argile/issues/220)
- Mise à jour de la clé d'encryption `NEXT_SERVER_ACTIONS_ENCRYPTION_KEY` dans le fichier README. [#222](https://github.com/MTES-MCT/fonds-prevention-argile/issues/222)
- Ajout d'actions. [#203](https://github.com/MTES-MCT/fonds-prevention-argile/issues/203)
