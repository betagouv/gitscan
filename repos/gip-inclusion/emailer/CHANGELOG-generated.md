## Changelog : emailer (30 derniers jours, au 21 septembre 2026)

### Résumé
Ce mois-ci, l'outil a considérablement enrichi sa capacité de génération d'e-mails avec l'ajout de nouveaux modèles (SIAE, prescripteurs et structures IAE). L'intégration avec le service Brevo a également été améliorée pour permettre une meilleure segmentation des campagnes.

### Évolutions fonctionnelles
- **Nouveaux modèles d'e-mails** : Mise à disposition de gabarits de référence pour les vues SIAE, prescripteurs, ainsi qu'une version de la vue "structure IAE" intégrant une charte partagée.
- **Optimisation de l'envoi Brevo** : Ajout de la gestion des tags de campagne (via l'option `--tag`) et simplification de l'objet des e-mails destinés aux prescripteurs.
- **Ajustement de contenu** : Révision de l'introduction des e-mails SIAE pour la rendre plus concise.

### Évolutions techniques
- **Refactorisation du code** : Renommage du script `render_contrats.py` en `render_prescripteurs.py` pour une meilleure cohérence avec les fonctionnalités actuelles.
- **Organisation des sorties** : Modification des chemins de dossiers par défaut (`out/SIAE-fins-contrats/`) afin de faciliter la gestion et la lisibilité lors de la génération de plusieurs e-mails simultanément.
