## Changelog : proconnect-env (30 derniers jours, au 12 novembre 2026)

### Résumé
L'outil a connu une transformation majeure avec le passage à une architecture entièrement statique. Cette évolution permet un hébergement simplifié tout en offrant une interface plus riche, avec des informations DNS plus détaillées et une meilleure clarté visuelle pour identifier l'environnement ProConnect actif.

### Évolutions fonctionnelles
- **Informations DNS enrichies** : Affichage des valeurs TTL (pour le CNAME et chaque serveur) via des infobulles.
- **Amélioration de la clarté visuelle** : 
    - Les indicateurs (aiguille et cartes) deviennent neutres (gris/non colorés) si le taux d'accord entre les serveurs DNS est inférieur à 60 %, évitant ainsi toute interprétation erronée.
    - Affichage de l'environnement RIE correspondant directement sous chaque carte.
- **Automatisation et interactivité** :
    - Mise en place d'un rafraîchissement automatique toutes les minutes (paramétrable via l'URL `?refresh=<seconds>`).
    - Stabilisation de la mise en page lors de la réception des données en streaming pour éviter les sauts visuels.
    - Amélioration de l'ergonomie du bouton de bascule "looking-glass".

### Évolutions techniques
- **Refonte architecturale complète** : Suppression du backend au profit d'une approche "client-only". L'application interroge désormais les résolveurs DNS directement depuis le navigateur via DNS-over-HTTPS, permettant un hébergement statique sur GitHub Pages [#3](https://github.com/proconnect-gouv/proconnect-env/pull/3).
- **Migration de domaine** : Le service est désormais accessible via le domaine personnalisé `env.proconnect.gouv.fr` [#2](https://github.com/proconnect-gouv/proconnect-env/pull/2).
- **Optimisation du flux de données** : Implémentation du streaming des réponses DNS et amélioration de la gestion des tentatives de reconnexion (retries).

### Autres changements
- **Documentation** : Mise à jour du fichier README.
- **Interface** : Ajustements textuels pour plus de neutralité (ex: utilisation de "ce serveur" au lieu de nommer explicitement le fournisseur d'hébergement).
