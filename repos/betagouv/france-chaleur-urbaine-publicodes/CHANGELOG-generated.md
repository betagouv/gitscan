## Changelog : france-chaleur-urbaine-publicodes (30 derniers jours)

### Résumé
Cette mise à jour apporte des améliorations au modèle Publicodes pour le comparateur France Chaleur Urbaine, notamment l'ajout de bilans sur une année pour certains types de systèmes de chauffage (PAC hybride, solaire thermique, solaire combiné). Des scripts ont également été ajoutés pour faciliter l'extraction de données intermédiaires et la publication du package sur npmjs.

### Évolutions fonctionnelles
- Ajout du bilan sur 1 an pour les systèmes de chauffage suivants : PAC hybride, solaire thermique et système solaire combiné.
- Amélioration de la documentation et du processus de publication sur npmjs.

### Évolutions techniques
- Mise à jour vers la version 1.4.0 du package.
- Mise à jour vers la version 1.3.0 du package.
- Configuration du système de publication pour utiliser un "trusted publisher" sur npmjs, supprimant la nécessité d'un token d'authentification.
- Ajout d'un script pour obtenir les tableaux intermédiaires de calcul.
- Complétion du script `external-keys` avec les paramètres du simulateur.

### Autres changements
- Rétractation temporaire de l'ajout du bilan 1 an pour la PAC hybride, le solaire thermique et le système solaire combiné (réversion du commit précédent).
