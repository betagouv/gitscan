## Changelog : grist-custom-forms (30 derniers jours, au 10 août 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec l'intégration complète du suivi des candidatures spontanées et l'optimisation du système de matching EURES. Les outils de communication, notamment via WhatsApp, ont été renforcés, et l'interface d'administration a été modernisée pour offrir une gestion plus fluide et une meilleure visibilité sur les interactions avec les employeurs et les candidats.

### Évolutions fonctionnelles
- **Gestion des candidatures spontanées** : Mise en place d'un suivi complet incluant la capture des réponses des employeurs, le suivi des candidatures de candidats, l'envoi d'emails de prospection et la documentation automatique dans le journal de projet.
- **Optimisation du matching EURES** : 
    - Amélioration de la prise de décision pour le matching manuel et clarification des badges de statut.
    - Meilleure gestion de la qualité des données (gestion des doublons de réponses, précision de la correspondance des salaires brut/net et amélioration de l'historique).
    - Interface optimisée avec une vue compacte de la liste de matching et de nouveaux filtres (ex: filtrage par employeur ayant répondu).
- **Communication & WhatsApp** : Ajout de la confirmation de numéro de téléphone pour les employeurs, affichage du statut WhatsApp dans les listes de matching et rétablissement du mécanisme de consentement pour les candidats.
- **Accès & Visibilité** : Rétablissement de l'accès public aux pages de projet et aux journaux de projet.

### Évolutions techniques
- **Administration & Performance** : 
    - Refonte complète de l'interface d'administration "Match Europe".
    - Correction des problèmes de délai d'attente (timeout) lors de l'envoi d'invitations groupées.
- **Stabilité & Fiabilité** : 
    - Mise en place de gardes de régression pour le module EURES.
    - Renforcement de la suite de tests, notamment pour les processus d'envoi d'emails et les actions de matching.
    - Amélioration des outils de nettoyage des invitations en double.
