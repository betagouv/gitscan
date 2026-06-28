## Changelog : Dossier-Facile-Frontend (30 derniers jours, au 26 juin 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à l'analyse de la taxe foncière, avec de nouveaux messages et un temps d'analyse augmenté pour plus de fiabilité. Des corrections ont également été apportées à la gestion de la déconnexion FranceConnect et à l'envoi des emails des co-locataires. Enfin, des améliorations ont été faites aux tests end-to-end pour une meilleure couverture et stabilité.

### Évolutions fonctionnelles
- **Taxe foncière :** Ajout de nouveaux messages d'analyse pour la taxe foncière, améliorant l'expérience utilisateur lors de la saisie de ces informations. [#1987](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1987)
- **Taxe foncière :** Augmentation du délai d'analyse de la taxe foncière pour éviter les erreurs dues à des traitements trop rapides. [#1989](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1989)
- **Co-locataires :** Correction d'un bug empêchant l'envoi de l'email des co-locataires à l'API lorsque les noms étaient déjà enregistrés. [#1934](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1934)
- **Déconnexion FranceConnect :** Correction d'un problème de déconnexion FranceConnect après la suppression d'un locataire. [#1991](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1991)
- **Watermark :** Ajout d'un compteur de caractères au message du watermark. [#1977](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1977)
- **Accessibilité :** Ajout d'une déclaration d'accessibilité. [#1980](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1980)

### Évolutions techniques
- **Tests E2E :** Ajout de scénarios de tests end-to-end pour les partenaires et les cas de refus. [#1985](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1985), [#1990](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1990)
- **Tests E2E :** Utilisation de l'inscription native au lieu de FranceConnect dans les tests end-to-end. [#1986](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1986)
- **Gestion des jobs E2E :** Correction pour éviter l'exécution concurrente des jobs de tests end-to-end. [#1984](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1984)
- **Version :** Mise à jour vers la version V3.5.11. [#1984](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1984)
- **Analyse :** Contournement temporaire de l'analyse pour l'auto-sauvegarde dans tenantv3. [#1992](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1992)

### Autres changements
- **Documentation :** Ajout d'un fichier `agent.md`. [#1981](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1981)
- **Message Honor Declaration :** Rétractation du message concernant la déclaration d'honneur. [#1988](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1988)
- **Composant Tax Property :** Création d'un composant personnalisé pour la propriété fiscale. [#1993](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1993)
