## Changelog : fonds-prevention-argile (30 derniers jours, au 22 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'espace agent, avec de nouvelles fonctionnalités pour la gestion des dossiers, l'accès aux informations et l'automatisation de certaines tâches. Des corrections ont également été apportées pour améliorer la stabilité et la sécurité de l'application, notamment concernant la gestion des parcours utilisateurs et les vulnérabilités de sécurité. Enfin, des améliorations ont été apportées à l'expérience utilisateur, comme l'ajout d'un kit de communication et la persistance des filtres dans l'espace agent.

### Évolutions fonctionnelles
- Les agents peuvent désormais consulter le détail des dossiers sans AMO. [#223](https://github.com/MTES-MCT/fonds-prevention-argile/issues/223)
- Ajout d'un kit de communication accessible via la route `/kit`. [#206](https://github.com/MTES-MCT/fonds-prevention-argile/issues/206)
- Les agents ont maintenant accès à tous les dossiers. [#199](https://github.com/MTES-MCT/fonds-prevention-argile/issues/199)
- Possibilité de copier les adresses email par onglet dans l'espace agent. [#204](https://github.com/MTES-MCT/fonds-prevention-argile/issues/204)
- Preremplissage de la démarche de diagnostic. [#216](https://github.com/MTES-MCT/fonds-prevention-argile/issues/216)
- Affichage du nom et prénom du demandeur dans `ds:probe-dossiers`. [#237](https://github.com/MTES-MCT/fonds-prevention-argile/issues/237)
- Le simulateur ne considère plus éligible un logement hors zone argileuse. [#215](https://github.com/MTES-MCT/fonds-prevention-argile/issues/215)
- Ajout d'une vue diagnostic des dossiers DN. [#228](https://github.com/MTES-MCT/fonds-prevention-argile/issues/228)
- Les filtres de dossiers dans l'espace agent sont maintenant persistés dans l'URL. [#205](https://github.com/MTES-MCT/fonds-prevention-argile/issues/205)

### Évolutions techniques
- Correction des CVE openssl de l'image de développement et réparation de la build Docker. [#227](https://github.com/MTES-MCT/fonds-prevention-argile/issues/227)
- Correction d'un bug où `relink` pouvait rattacher une cible à un parcours existant. [#238](https://github.com/MTES-MCT/fonds-prevention-argile/issues/238)
- Correction d'erreurs de synchronisation DN. [#229](https://github.com/MTES-MCT/fonds-prevention-argile/issues/229)
- Correction de la logique de l'URL dans les parcours. [#197](https://github.com/MTES-MCT/fonds-prevention-argile/issues/197)
- Script pour réinitialiser un dossier en validation AMO. [#219](https://github.com/MTES-MCT/fonds-prevention-argile/issues/219)
- Correction d'un script `relink`. [#236](https://github.com/MTES-MCT/fonds-prevention-argile/issues/236)

### Autres changements
- Mise à jour de la documentation pour les agents. [#202](https://github.com/MTES-MCT/fonds-prevention-argile/issues/202)
- Mise à jour de la clé `NEXT_SERVER_ACTIONS_ENCRYPTION_KEY` dans le README. [#222](https://github.com/MTES-MCT/fonds-prevention-argile/issues/222)
- Mise à jour de la configuration Matomo. [#217](https://github.com/MTES-MCT/fonds-prevention-argile/issues/217)
- Utilisation du nom de famille et non uniquement du nom de jeune fille dans l'application. [#200](https://github.com/MTES-MCT/fonds-prevention-argile/issues/200)
- Bump de version à 1.14.0. [#220](https://github.com/MTES-MCT/fonds-prevention-argile/issues/220)
- Mise à jour des dépendances. [#224](https://github.com/MTES-MCT/fonds-prevention-argile/issues/224)
- Correction d'un problème de parcours orphelins. [#198](https://github.com/MTES-MCT/fonds-prevention-argile/issues/198)
