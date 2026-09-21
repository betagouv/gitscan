## Changelog : sps-emailer (30 derniers jours, au 10 septembre 2026)

### Résumé
Cette période a été marquée par une avancée majeure dans la création de modèles d'e-mails personnalisés. Le projet dispose désormais de nouveaux gabarits de référence pour les différents destinataires (SIAE, prescripteurs et structures IAE) et bénéficie d'une meilleure intégration avec l'outil d'envoi Brevo pour faciliter la gestion des campagnes.

### Évolutions fonctionnelles
- **Nouveaux modèles d'e-mails** : Mise en place de gabarits de référence pour le rendu des vues destinées aux SIAE, aux prescripteurs et aux structures IAE (incluant une charte partagée).
- **Amélioration de l'envoi (Brevo)** : Ajout de la gestion des tags de campagne et simplification de l'objet des e-mails pour les prescripteurs.
- **Optimisation du contenu** : Ajustement du texte d'introduction des e-mails SIAE pour plus de concision.

### Évolutions techniques
- **Refactorisation** : Renommage du fichier `render_contrats.py` en `render_prescripteurs.py` pour une meilleure cohérence avec les fonctionnalités du projet.
- **Organisation des fichiers** : Modification des chemins de sortie par défaut pour améliorer la lisibilité lors de la génération de plusieurs e-mails.
